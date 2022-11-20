
import os
import shutil
import subprocess
import platform


from src.domain.project_t import Project_t
from src.domain.types.dir_t import Dir_t
from src.domain.config_t import Config_t
from src.domain.builder_t import Builder_i
from src.domain.types.dict_smart_t import DictSmart_t
from src.domain.tree_t import Tree_t
from src.domain.types.dependencie_t import Dependencie_t
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e

from src.ports.messages.message_handler import Message_Handler as MH

import src.tools.file as FILE_TOOL
import src.tools.include as INCLUDE_TOOL
import src.tools.string as STRING_TOOL
import src.tools.os as OS_TOOL

class Cmake_t(Builder_i):
    def __init__(self):
        super().__init__()

    def create_project_api(self, next_dir: Dir_t, this_dir: Dir_t, name_project: str, data: DictSmart_t) -> StatusCode_t:
        build_dir=data['build_dir']
        type_project=data['type_project']
        name_build=data['name_build']
        build_system=data['build_system']
        build_system_exe=data['build_system_exe']
        c_compiler=data['c_compiler']
        cxx_compiler=data['cxx_compiler']
        
        # Message(Waiting): Create a proyect of next in
        MH.message_waiting('Create a proyect of next in: ' + this_dir.path() + '/' + name_project)
        
        try:
            # Default Type Proyect
            base_project = "empty_executable/"

            # Get nextEmptyProjectDir
            next_empty_project_dir = next_dir.path() + "/assets/" + base_project

            # Copy the nextEmptyProjectDir in new project {name}
            shutil.copytree(next_empty_project_dir, name_project, dirs_exist_ok=True)

            # View the dir of new project {name}
            dir_new_project = this_dir.path() + "/" + name_project

            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__build_dir__", build_dir)

            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__name_project__", name_project)
            FILE_TOOL.remplace_in_file(dir_new_project + "/CMakeLists.txt", "__name_project__", name_project)


            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__name_build__", name_build)
            FILE_TOOL.remplace_in_file(dir_new_project + "/CMakeLists.txt", "__name_build__", name_build)
            
            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__build_system_exe__", build_system_exe)
            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__build_system__", build_system)
            
            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__c_compiler__", c_compiler)
            

            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__cxx_compiler__", cxx_compiler)
            
            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__type_project__", type_project)
                
            # Message(Successful): Create a proyect of next in
            MH.message_successful('Create a proyect of next in: ' + this_dir.path() + '/' + name_project)
            return StatusCodes_e.SUCCESSFUL

        except OSError as exc:
        
            # Message(Error): OSError generate
            MH.message_error(str(exc))
            return StatusCodes_e.ERROR

    def create_project(self, next_dir: Dir_t, this_dir: Dir_t, name_project: str) -> StatusCode_t:

        data = DictSmart_t('')

        _, data['build_dir']=MH.message_question('Build Dir: ', defaultAnswer='build', printDefault=True)
        _, data['type_project']=MH.message_question('Type Project: ', defaultAnswer='executable', listAnswer=['executable', 'static_library', 'dynamic_library'], printDefault=True)
        _, data['name_build']=MH.message_question('Name Build: ', defaultAnswer='app', printDefault=True)
        _, data['build_system']=MH.message_question('Build System: ', defaultAnswer='Ninja', printDefault=True)
        _, data['build_system_exe']=MH.message_question('Build System Executable: ', defaultAnswer='ninja', printDefault=True)
        _, data['c_compiler']=MH.message_question('C Compiler: ', defaultAnswer='gcc', printDefault=True)
        _, data['cxx_compiler']=MH.message_question('C++ Compiler: ', defaultAnswer='g++', printDefault=True)
        
        return self.create_project_api(next_dir=next_dir, this_dir=this_dir, name_project=name_project, data=data)

    _list_includes = []
    _list_libraries = []

    def _getIncludes(dependencie: Dependencie_t, num_deep: int , args:dict):
        if dependencie.includes != '':
            args['_list_includes'] += dependencie.includes
        
    def _getLibraries(dependencie: Dependencie_t, num_deep: int , args:dict):
        if dependencie.library != '':
            args['_list_libraries'].append(dependencie.library)


    def _generateCommand(
            self,
            dir: str, 
            build_system: str, 
            type_project: str, 
            c_compiler: str, 
            cxx_compiler: str, 
            cmake_flags: list,
            include_dirs: list,
            libs: list
            ):

        command = []

        # Add Cmake executable
        command.append ("cmake")

        # Add Directory of project
        command.append(dir + "/.")

        # Add BuildSystem
        if(STRING_TOOL.countWord(build_system) == 1 or platform.system() == 'Linux'):
            command.append( "-G"  + build_system  )
        else: 
            
            command.append( "-G" + "\"" + build_system + "\""  )

        # Add C compiler
        command.append( "-DCMAKE_C_COMPILER=" + c_compiler )

        # Add C++ compiler
        command.append( "-DCMAKE_CXX_COMPILER=" + cxx_compiler)

        # Add type Project
        command.append( "-D" + type_project + "=on" )

        # Add cmake_flags
        command += cmake_flags

        #Add inlucde Local
        if len(include_dirs) > 0:
            command.append( "-DINCLUDE_LOCAL=\"" + STRING_TOOL.listToStr(include_dirs, separator=";") + "\"" )
        
        #Add libs Local
        if len(libs) > 0:
            command.append( "-DEXTERN_LIBS=" + STRING_TOOL.listToStr(libs, separator=";")  )

        return command

    def _generateCommadBuildSystem(
        self,
        build_system_exce: str,
        build_system_flags: str
    ):
        command = []

        # Add build system executable
        command.append( build_system_exce )

        # Add build system flags
        command += build_system_flags

        return command


    def build(self, project: Project_t, name_build: str) -> StatusCode_t:
        return self.build_api(project=project, name_build=name_build)


    def build_api(self, project: Project_t, name_build: str):

        config_obj: Config_t = project.config
        config_build = config_obj.get('builds')[name_build]
        build_dir = config_obj.get("build_dir")
        build_name = config_obj.get("build_name")
        this_dir = project.path.path()

        OS_TOOL.mkdirDir(Dir_t(build_dir))
        # Into in the directory of build
        os.chdir(build_dir)
        # Mkdir build_dir
        OS_TOOL.mkdirDir(Dir_t(name_build))
        #os.mkdir(self.build_name)
        os.chdir(name_build)

        # Get the include local
        include_local = INCLUDE_TOOL.get_includes(Dir_t(this_dir))

        # Get the Tree
        tree = Tree_t(Dir_t(this_dir))
        # Get INcludes of Project and dependencies
        tree.deepTravers(Cmake_t._getIncludes, args = {'_list_includes': Cmake_t._list_includes})
        # Get libs and dependencies
        tree.deepTravers(Cmake_t._getLibraries, args = {'_list_libraries': Cmake_t._list_libraries})

        # Desactivate the output
        MH.OUTPUT_ACTIVATED = False
        
        # create command of Cmake
        command = self._generateCommand(
                dir=this_dir,
                build_system=config_build["build_system"],
                c_compiler=config_build["c_compiler"],
                cxx_compiler=config_build["cxx_compiler"],
                type_project=config_obj.get("type_project"),
                cmake_flags=config_build["cmake_flags"],
                include_dirs=include_local + Cmake_t._list_includes,
                libs=Cmake_t._list_libraries
            )

        # Run the Cmake Command
        subprocess.run(command)

        # Create command of build system
        buildSystemCommand = self._generateCommadBuildSystem(
            build_system_exce=config_build["build_system_exe"],
            build_system_flags=config_build["build_system_flags"]
        )
        # Run the command of build system
        subprocess.run(buildSystemCommand)


        MH.OUTPUT_ACTIVATED = True
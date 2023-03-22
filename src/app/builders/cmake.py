######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 06/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import os
import shutil
from src.domain.types.dir_t import Dir_t
from src.domain.project_t import Project_t

from src.ports.messages.message_handler import Message_Handler as MH

import src.tools.file as FILE_TOOL

def create_cmake(
    next_dir:str, 
    this_dir:str,
    name_project:str,
    ):
    _, build_dir=MH.message_question('Build Dir: ', defaultAnswer='build', printDefault=True)
    _, type_project=MH.message_question('Type Project: ', defaultAnswer='executable', listAnswer=['executable', 'static_library', 'dynamic_library'], printDefault=True)
    _, name_build=MH.message_question('Name Build: ', defaultAnswer='app', printDefault=True)
    _, build_system=MH.message_question('Build System: ', defaultAnswer='Ninja', printDefault=True)
    _, build_system_exe=MH.message_question('Build System Executable: ', defaultAnswer='ninja', printDefault=True)
    _, c_compiler=MH.message_question('C Compiler: ', defaultAnswer='gcc', printDefault=True)
    _, cxx_compiler=MH.message_question('C++ Compiler: ', defaultAnswer='g++', printDefault=True)
    
    # Message(Waiting): Create a proyect of next in
    MH.message_waiting('Create a proyect of next in: ' + this_dir + '/' + name_project)
    
    try:
        # Default Type Proyect
        base_project = "empty_executable/"

        # Get nextEmptyProjectDir
        next_empty_project_dir = next_dir + "/assets/" + base_project

        # Copy the nextEmptyProjectDir in new project {name}
        shutil.copytree(next_empty_project_dir, name_project, dirs_exist_ok=True)

        # View the dir of new project {name}
        dir_new_project = os.getcwd() + "/" + name_project

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
        MH.message_successful('Create a proyect of next in: ' + this_dir + '/' + name_project)

    except OSError as exc:
        
        # Message(Error): OSError generate
        MH.message_error(str(exc))



from src.domain.config_t import Config_t
from src.ports.messages.message_handler import Message_Handler as MH
import src.tools.include as INCLUDE_TOOL
import src.tools.string as STRING_TOOL
import src.tools.os as OS_TOOL
from src.domain.tree_t import Tree_t
from src.domain.types.dependencie_t import Dependencie_t

#System Packages
import subprocess
import os
import platform

_list_includes = []
_list_libraries = []

def _getIncludes(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.includes != '':
        args['_list_includes'] += dependencie.includes
    
def _getLibraries(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.library != '':
        args['_list_libraries'].append(dependencie.library)


def _generateCommand(
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
    build_system_exce: str,
    build_system_flags: str
):
    command = []

    # Add build system executable
    command.append( build_system_exce )

    # Add build system flags
    command += build_system_flags

    return command





def build_cmake(project: Project_t, name_build: str):

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
    tree.deepTravers(_getIncludes, args = {'_list_includes': _list_includes})
    # Get libs and dependencies
    tree.deepTravers(_getLibraries, args = {'_list_libraries': _list_libraries})

    # Desactivate the output
    MH.OUTPUT_ACTIVATED = False
    
    # create command of Cmake
    command = _generateCommand(
            dir=this_dir,
            build_system=config_build["build_system"],
            c_compiler=config_build["c_compiler"],
            cxx_compiler=config_build["cxx_compiler"],
            type_project=config_obj.get("type_project"),
            cmake_flags=config_build["cmake_flags"],
            include_dirs=include_local + _list_includes,
            libs=_list_libraries
        )

    # Run the Cmake Command
    subprocess.run(command)

    # Create command of build system
    buildSystemCommand = _generateCommadBuildSystem(
        build_system_exce=config_build["build_system_exe"],
        build_system_flags=config_build["build_system_flags"]
    )
    # Run the command of build system
    subprocess.run(buildSystemCommand)


    MH.OUTPUT_ACTIVATED = True
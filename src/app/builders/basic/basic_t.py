
import os
import shutil
import stat
import platform


from src.domain.project_t import Project_t
from src.domain.types.dir_t import Dir_t
from src.domain.config_t import Config_t
from src.domain.builder_t import Builder_i
from src.domain.types.dict_smart_t import DictSmart_t
from src.domain.types.null_smart_t import NullSmart_t
from src.domain.tree_t import Tree_t
from src.domain.types.dependencie_t import Dependencie_t
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e

from src.ports.messages.message_handler import Message_Handler as MH

import src.tools.file as FILE_TOOL
import src.tools.include as INCLUDE_TOOL
import src.tools.string as STRING_TOOL
import src.tools.os as OS_TOOL

# Open script of bash
SYSTEM = platform.system()


_COMMENTS_CHAR = '#'
_FILE_BASIC_BUILD_SH = 'basic_build.sh'
_SLASH_CHAR = '/'

if SYSTEM != 'Linux':
    _COMMENTS_CHAR = '::'
    _FILE_BASIC_BUILD_SH = 'basic_build.bat'
    _SLASH_CHAR = '\\'


_list_includes = []
_list_libraries = []

def _getIncludes(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.includes != '':
        args['_list_includes'] += dependencie.includes
    
def _getLibraries(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.library != '':
        print('Hola')
        args['_list_libraries'].append(dependencie.library)

class Basic_t(Builder_i):
    def __init__(self):
        super().__init__()

    def create_project_api(self, next_dir: Dir_t, this_dir: Dir_t, name_project: str, data: DictSmart_t) -> StatusCode_t:
        build_dir=data['build_dir']
        type_project=data['type_project']
        name_build=data['name_build']
        
        # Message(Waiting): Create a proyect of next in
        MH.message_waiting('Create a proyect of next in: ' + this_dir.path() + '/' + name_project)
        
        try:
            # Default Type Proyect
            base_project = "base_builders_projects/basic/executable/"

            # Get nextEmptyProjectDir
            next_empty_project_dir = next_dir.path() + "/assets/" + base_project

            # Copy the nextEmptyProjectDir in new project {name}
            shutil.copytree(next_empty_project_dir, name_project, dirs_exist_ok=True)

            # View the dir of new project {name}
            dir_new_project = this_dir.path() + "/" + name_project

            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__build_dir__", build_dir)

            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__name_project__", name_project)


            FILE_TOOL.remplace_in_file(dir_new_project + "/config.yaml", "__build_name__", name_build)
            
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
        
        return self.create_project_api(next_dir=next_dir, this_dir=this_dir, name_project=name_project, data=data)

    config_build = {}
    this_dir = ""
    build_name = ""
    config_obj: Config_t

    def _generateCommand(
        dir: str, 
        build_dir: str,
        builder_name: str,
        type_project: str,
        name_out: str,
        c_compiler: str, 
        cxx_compiler: str,
        linker: str,
        ar: str,
        c_compiler_regex: str,
        cxx_compiler_regex: str,
        linker_regex: str,
        static_linker_regex: str,
        dynamic_linker_regex: str,
        include_dirs: list,
        libs: list,
        c_source: list,
        cxx_source: list,
        extension_files: list
        ):
        # Get Our Files from dict    
        def getOutFiles(compile_lines: list):
            lines = []
            for file in compile_lines:
                lines.append(file['path_file_out'])
            return lines
        
        # Generate compile lines with format $CXX -c $FILE -o $FILE_OUT
        def generate_compile_lines(source: list, compiler_hash: str, compiler: str, compiler_regex: str):
            
            compile_lines = []
            
            for file in source:
                
                #Init with regex
                line_compile = compiler_regex
                
                # Remplace compiler example: $CXX -c $FILE -o $FILE_OUT -> g++ -c $FILE -o $FILE_OUT
                line_compile = line_compile.replace(compiler_hash, compiler)
                
                # Create path of output file
                path_file_out = dir + _SLASH_CHAR + build_dir + _SLASH_CHAR + builder_name + file.replace(dir, '') + '.o'
                
                # Remove extension of source code example: main.cpp.o -> main.o
                for ext in extension_files:
                    path_file_out = path_file_out.replace(ext + '.o', '.o')
                
                # Remplace path of output file example: g++ -c $FILE -o $FILE_OUT -> g++ -c $FILE -o build/basic/main.o
                line_compile = line_compile.replace('$FILE_OUT', path_file_out)
                line_compile = line_compile.replace('$FILE', file)
                
                # Add Include dirs
                for i in include_dirs:
                    line_compile += ' -I' + i
                
                if SYSTEM != 'Linux':
                    line_compile = line_compile.replace('/', '\\')
                    path_file_out = path_file_out.replace('/', '\\')

                
                # Apped dict of data in compile_lines
                compile_lines.append(
                    {
                        'line_compile':line_compile, 
                        'path_file_out': path_file_out
                    }
                )
                
            return compile_lines
                
        # Create compile lines of C++
        cxx_compile_lines = generate_compile_lines(
            source          = cxx_source, 
            compiler_hash   = '$CXX', 
            compiler        = cxx_compiler, 
            compiler_regex  = cxx_compiler_regex,
            )
        
        # Create compile lines of C
        c_compile_lines = generate_compile_lines(
            source          = c_source, 
            compiler_hash   = '$C', 
            compiler        = c_compiler, 
            compiler_regex  = c_compiler_regex
            )
            

        # Add linker
        
        if type_project == 'executable':
            linker_line = linker_regex
            linker_line = linker_line.replace('$LD', linker)
        elif type_project == 'static_library':
            linker_line = static_linker_regex
            linker_line = linker_line.replace('$AR', ar)
        elif type_project == 'dynamic_library':
            linker_line = dynamic_linker_regex
            linker_line = linker_line.replace('$LD', linker)
        #Add Filer out
        linker_line = linker_line.replace(
            '$FILES', 
            STRING_TOOL.listToStr(getOutFiles(cxx_compile_lines) + getOutFiles(c_compile_lines), separator=' '))
        
        #Add final file
        linker_line = linker_line.replace('$FILE_OUT', name_out)
        if type_project == 'executable':
            # Add Include dirs
            for i in include_dirs:
                linker_line += ' -I' + i
            
            # Add Libraries 
            for lib in libs:
                linker_line += ' ' + lib
            
        # Open script of bash
        if SYSTEM != 'Linux':
            f = open( 'basic_build.bat', 'w')
        else:
            f = open( 'basic_build.sh', 'w')
            
        # Write lines to compile
        for file in cxx_compile_lines + c_compile_lines:
            
            # Create dirs
            index_dirs_of_file = file['path_file_out'].rfind('/')
            OS_TOOL.mkdirDir(file['path_file_out'][:index_dirs_of_file])
            
            # Write Message
            f.write( _COMMENTS_CHAR + 'Generate: ' + file['path_file_out'] + '\n')
            
            # Write line to compile
            f.write(file['line_compile'] + '\n\n')
            
        
        # Write Message 
        f.write( _COMMENTS_CHAR + 'Generate: ' + name_out + '\n')
        
        # Write linker line
        f.write( linker_line + '\n')
            
        f.close()
        
        # Change permise of file
        if SYSTEM != 'Windows':
            st = os.stat( 'basic_build.sh')
            os.chmod( 'basic_build.sh', st.st_mode | stat.S_IEXEC)
            # Run script
            os.system('bash -x ' + dir + '/' + build_dir + '/' + builder_name + '/' + 'basic_build.sh' )
        else:
            os.system( dir + _SLASH_CHAR + build_dir + _SLASH_CHAR + builder_name + _SLASH_CHAR + 'basic_build.bat' )

        
        
        return
    
    
    def _getSource(self, source_name='source_c') -> list:
        """Get All path of files source

        Args:
            source_name (str, optional): Name of Sources. Defaults to 'source_c'.

        Returns:
            list: All Files of sources
        """
        
        # All Files of sources
        source_list = []
        
        # Data List Encode of ruamel.yaml
        source = NullSmart_t.type_is()
        try:
            
            # Get Data List
            source = self.config_build[source_name]
        except KeyError as exc:
            
            # Message(SuperWarning): OSError generate
            # TODO: Hacer una funcion MH.super_message_* que muestre el output simpre aunque MH.OUTPUT_ACTIVATED = False
            MH.message_error('No Find: builds.' + self.build_name + '.' + source_name + ' in ' + self.this_dir + '/config.yaml')
            
            # Return void List
            return []
        
        # Loop for get files
        for s in source:
            
            # If explicit path
            if s.find('*') == -1:
                
                # Create full path
                s_file_path = self.this_dir + _SLASH_CHAR + s
                
                # Check if s_file_path is a FIle and exists
                if os.path.isfile(s_file_path):
                    
                    # Add File in source_list
                    source_list.append(s_file_path)
                else:
                    
                    # Message(SuperWarning): OSError generate
                    MH.message_error(s_file_path + ' Not is a File')

            else:
                
                # Get index recursive in string
                index_str_recursive = s.find('*')
                
                # Save extension Files
                extension_files = s[index_str_recursive + 1:]
                
                # Copy left side of string
                s = s[:index_str_recursive]
                
                # Create full path of Dir
                s_dir_path = self.this_dir + _SLASH_CHAR + s
                
                #Apped files with extension
                source_list += OS_TOOL.find_files_for_ext(dir=s_dir_path,ext=extension_files)
            
        return list(set(source_list))

    def makeDirs_of_source(self, source: list[str], build_dir: str) -> StatusCode_t:
        for s in source:
            s = s[::-1]
            for i in range(len(s)):
                if s[i] == _SLASH_CHAR:
                    new_s = s[i:-1]
                    if SYSTEM != 'Linux':
                        new_s = new_s[:-1]
                    new_s = _SLASH_CHAR + new_s[::-1]
                    if SYSTEM != 'Linux':
                        new_s = self.this_dir + _SLASH_CHAR + build_dir + _SLASH_CHAR + self.build_name + new_s.replace(self.this_dir[2:], '')
                    else:
                        new_s = self.this_dir + _SLASH_CHAR + build_dir + _SLASH_CHAR + self.build_name + new_s.replace(self.this_dir, '')
                    OS_TOOL.makeDirs(Dir_t(new_s))
                    break
    
    def build(self,project: Project_t, name_build: str):

        self.config_obj = project.config
        
        self.config_build = self.config_obj.get('builds')[name_build]

        self.this_dir = project.path.path()

        self.build_name = name_build

        OS_TOOL.mkdirDir(Dir_t(self.config_obj.get("build_dir")))

        # Into in the directory of build
        os.chdir(self.config_obj.get("build_dir"))
        
        # Mkdir build_dir
        OS_TOOL.mkdirDir(Dir_t(self.build_name))
        
        #os.mkdir(self.build_name)
        os.chdir(self.build_name)

        # Get the include local
        include_local = INCLUDE_TOOL.get_includes(Dir_t(self.this_dir))

        # Get the Tree
        tree = Tree_t(Dir_t(self.this_dir))
        # Get Includes of Project and dependencies
        #tree.deepTravers(_getIncludes, args = {'_list_includes': _list_includes})

        # Get libs and dependencies
        #tree.deepTravers(_getLibraries, args = {'_list_libraries': _list_libraries})

        #print(_list_libraries)
        # Desactivate the output
        # TODO: esta linea debe cambiarse a MH.output_deactivate() y su contraria MH.output_activate()
        # para evitar que MH.OUTPUT_ACTIVATED se asigne aun tipo no bool
        MH.OUTPUT_ACTIVATED = True
        
        sourceCXX = self._getSource('source_cxx')
        sourceC = self._getSource('source_c')

        sourceAll = sourceCXX + sourceC

        if SYSTEM != 'Linux':
            for i in range(len(sourceAll)):
                sourceAll[i] = sourceAll[i].replace('/', _SLASH_CHAR)

        self.makeDirs_of_source(source=sourceAll, build_dir=self.config_obj.get("build_dir"))

        type_project = self.config_obj.get('type_project')
        defaul_c_compiler_regex = ''
        defaul_cxx_compiler_regex = ''
        c_compiler = self.config_build.get("c_compiler")           if self.config_build.get("c_compiler")          != None else 'gcc'
        cxx_compiler = self.config_build.get("cxx_compiler")       if self.config_build.get("cxx_compiler")        != None else 'g++'
        linker = self.config_build.get("linker")                   if self.config_build.get("linker")              != None else 'g++'
        ar = self.config_build.get("ar")                           if self.config_build.get("ar")                  != None else 'ar'
        linker_regex = self.config_build.get("linker_regex")         if self.config_build.get("linker_regex")        != None else '$LD $FILES -o $FILE_OUT'
        static_linker_regex = self.config_build.get("static_linker_regex")  if self.config_build.get("static_linker_regex") != None else '$AR rcs $FILE_OUT $FILES'
        dynamic_linker_regex = self.config_build.get("dynamic_linker_regex") if self.config_build.get("dynamic_linker_regex")!= None else '$LD $FILES -shared -o $FILE_OUT'
        include_dirs = list(set(include_local + _list_includes))
        libs = list(set(_list_libraries))

        if self.config_build.get("type_build") != None:
            type_project = self.config_build.get("type_build")


        if self.config_build.get("c_compiler_regex") != None:
            defaul_c_compiler_regex = self.config_build.get("c_compiler_regex")

        if self.config_build.get("cxx_compiler_regex") != None:
            defaul_cxx_compiler_regex = self.config_build.get("cxx_compiler_regex")
        
        if type_project == 'dynamic_library': 
            if defaul_c_compiler_regex      ==   '': defaul_c_compiler_regex    = '$C -fPIC -c $FILE -o $FILE_OUT'
            if defaul_cxx_compiler_regex    ==   '': defaul_cxx_compiler_regex  = '$CXX -fPIC -c $FILE -o $FILE_OUT'
        elif type_project == 'static_library':
            if defaul_c_compiler_regex      ==   '': defaul_c_compiler_regex    = '$C -c $FILE -o $FILE_OUT'
            if defaul_cxx_compiler_regex    ==   '': defaul_cxx_compiler_regex  = '$CXX -c $FILE -o $FILE_OUT'
        else:
            if defaul_c_compiler_regex      ==   '': defaul_c_compiler_regex    = '$C -c $FILE -o $FILE_OUT'
            if defaul_cxx_compiler_regex    ==   '': defaul_cxx_compiler_regex  = '$CXX -c $FILE -o $FILE_OUT'

        MH.message_waiting('Build Project')        
        print('     Dir            -> ' + self.this_dir)
        print('     BuilderName    -> ' + self.build_name)
        print('     NameOut        -> ' + self.config_build.get("name_out")           if self.config_build.get("name_out")          != None else self.build_name)
        print('     BuildDir       -> ' + self.config_obj.get('build_dir'))
        print('     TypeProject    -> ' + type_project)
        print('     C Compiler     -> ' + c_compiler)
        print('     C++ Compiler   -> ' + cxx_compiler)
        print('     Linker         -> ' + linker)
        print('     AR Linker      -> ' + ar)
        print('     Dynamic Linker -> ' + linker)
        print('     C Regex        -> ' + defaul_c_compiler_regex)
        print('     C++ Regex      -> ' + defaul_cxx_compiler_regex)
        print('     Linker Regex   -> ' + linker_regex)
        print('     Static Regex   -> ' + static_linker_regex)
        print('     Dynamic Regex  -> ' + dynamic_linker_regex)
        print('     Includes:')
        STRING_TOOL.printList(include_dirs, pre = '       - ')
        print('     Libs:')
        STRING_TOOL.printList(libs, pre = '       - ')

        
        # create command of Basic
        Basic_t._generateCommand(
                dir                 = self.this_dir,
                builder_name        = self.build_name,
                name_out            = self.config_build.get("name_out")           if self.config_build.get("name_out")          != None else self.build_name,
                build_dir           = self.config_obj.get('build_dir'),
                type_project        = type_project,
                c_compiler          = c_compiler,
                cxx_compiler        = cxx_compiler,
                linker              = linker,
                ar                  = self.config_build.get("ar")                   if self.config_build.get("ar")                  != None else 'ar',
                c_compiler_regex    = defaul_c_compiler_regex,
                cxx_compiler_regex  = defaul_cxx_compiler_regex,
                linker_regex        = linker_regex,
                static_linker_regex = static_linker_regex,
                dynamic_linker_regex= dynamic_linker_regex,
                extension_files     = self.config_build.get("extension_files")      if self.config_build.get("extension_files" )    != None else ['.c', '.cc', '.cpp'],
                c_source            = sourceC,
                cxx_source          = sourceCXX,
                include_dirs        = include_dirs,
                libs                = libs,
            )

        MH.OUTPUT_ACTIVATED = True

    def validate_build(self, project: Project_t, name_build: str):
        self.config_obj = project.config

        self.config_build = self.config_obj.get('builds')[name_build]

        exit_flag = False

        if 'name_out' not in self.config_build:
            MH.message_unknown(f'Not find property \'name_out\' of type \'str\' in Build: {name_build}')
            exit_flag = True
        if 'source_cxx' not in self.config_build:
            MH.message_unknown(f'Not find property \'source_cxx\' of type \'list\' in Build: {name_build}')
        if 'source_c' not in self.config_build:
            MH.message_unknown(f'Not find property \'source_c\' of type \'list\' in Build: {name_build}')

        if exit_flag:
            exit()
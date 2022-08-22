######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 15/08/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
import os
import stat

# Local Packages

from src.models.config_t import config_t as Config_t
import src.tool.messages as MESSAGES_tools
import src.funcs.includes as INCLUDE_funcs
import src.tool.string as STRING_tools
import src.tool.types as TYPES_tools
import src.tool.os as OS_tools
from src.models.tree_t import Tree_t as Tree_t
from src.models.tree_t import Dependencie_t as Dependencie_t

import bash

_list_includes = []
_list_libraries = []

def _getIncludes(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.include != '':
        args['_list_includes'] += dependencie.include
    
def _getLibraries(dependencie: Dependencie_t, num_deep: int , args:dict):
    if dependencie.library != '':
        args['_list_libraries'].append(dependencie.library)

class Basic_t:
    
    config_build = {}
    this_dir = ""
    build_name = ""
    
    def __init__(self, config_build, this_dir, build_name=""):
        self.config_build = config_build
        self.this_dir = this_dir
        self.build_name = build_name

    def _generateCommand(
        dir: str, 
        build_dir: str,
        builder_name: str,
        name_out: str,
        type_project: str, 
        c_compiler: str, 
        cxx_compiler: str,
        linker: str,
        c_compiler_regex: str,
        cxx_compiler_regex: str,
        linker_regex: str,
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
                path_file_out = dir + '/' + build_dir + '/' + builder_name + file.replace(dir, '') + '.o'
                
                # Remove extension of source code example: main.cpp.o -> main.o
                for ext in extension_files:
                    path_file_out = path_file_out.replace(ext + '.o', '.o')
                
                # Remplace path of output file example: g++ -c $FILE -o $FILE_OUT -> g++ -c $FILE -o build/basic/main.o
                line_compile = line_compile.replace('$FILE_OUT', path_file_out)
                line_compile = line_compile.replace('$FILE', file)
                
                # Add Include dirs
                for i in include_dirs:
                    line_compile += ' -I' + i
                
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
        linker_line = linker_regex
        
        linker_line = linker_line.replace('$LD', linker)
        
        #Add Filer out
        linker_line = linker_line.replace(
            '$FILES', 
            STRING_tools.listToStr(getOutFiles(cxx_compile_lines) + getOutFiles(c_compile_lines), separator=' '))
        
        #Add final file
        linker_line = linker_line.replace('$FILE_OUT', name_out)
        
        # Add Include dirs
        for i in include_dirs:
            linker_line += ' -I' + i
            
        # Add Libraries 
        for lib in libs:
            linker_line += ' ' + lib
            
        # Open script of bash
        f = open( 'basic_build.sh', 'w')
            
        # Write lines to compile
        for file in cxx_compile_lines + c_compile_lines:
            
            # Create dirs
            index_dirs_of_file = file['path_file_out'].rfind('/')
            OS_tools.mkdirDir(file['path_file_out'][:index_dirs_of_file])
            
            # Write Message
            f.write( '#Generate: ' + file['path_file_out'] + '\n')
            
            # Write line to compile
            f.write(file['line_compile'] + '\n\n')
            
        
        # Write Message 
        f.write( '#Generate: ' + name_out + '\n')
        
        # Write linker line
        f.write( linker_line + '\n')
            
        f.close()
        
        # Change permise of file
        st = os.stat( 'basic_build.sh')
        os.chmod( 'basic_build.sh', st.st_mode | stat.S_IEXEC)
        
        # Run script
        bash.bash(dir + '/' + build_dir + '/' + builder_name + '/' + 'basic_build.sh')
                
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
        source = TYPES_tools.NullType()
        try:
            
            # Get Data List
            source = self.config_build[source_name]
        except KeyError as exc:
            
            # Message(SuperWarning): OSError generate
            # TODO: Hacer una funcion MESSAGES_tools.super_message_* que muestre el output simpre aunque MESSAGES_tools.OUTPUT_ACTIVATED = False
            MESSAGES_tools.message_error('No Find: builds.' + self.build_name + '.' + source_name + ' in ' + self.this_dir + '/config.yaml')
            
            # Return void List
            return []
        
        # Loop for get files
        for s in source:
            
            # If explicit path
            if s.find('*') == -1:
                
                # Create full path
                s_file_path = self.this_dir + '/' + s
                
                # Check if s_file_path is a FIle and exists
                if os.path.isfile(s_file_path):
                    
                    # Add File in source_list
                    source_list.append(s_file_path)
                else:
                    
                    # Message(SuperWarning): OSError generate
                    MESSAGES_tools.message_error(s_file_path + ' Not is a File')

            else:
                
                # Get index recursive in string
                index_str_recursive = s.find('*')
                
                # Save extension Files
                extension_files = s[index_str_recursive + 1:]
                
                # Copy left side of string
                s = s[:index_str_recursive]
                
                # Create full path of Dir
                s_dir_path = self.this_dir + '/' + s
                
                #Apped files with extension
                source_list += OS_tools.find_files_for_ext(dir=s_dir_path,ext=extension_files)
            
        return list(set(source_list))
    
    def build(self,config_obj: Config_t):
        
        # Into in the directory of build
        os.chdir(config_obj.get("build_dir"))
        
        # Mkdir build_dir
        OS_tools.mkdirDir(self.build_name)
        
        #os.mkdir(self.build_name)
        os.chdir(self.build_name)

        # Get the include local
        include_local = INCLUDE_funcs.get_includes(self.this_dir)

        # Get the Tree
        tree = Tree_t(self.this_dir)
        
        # Get Includes of Project and dependencies
        tree.deepTravers(_getIncludes, args = {'_list_includes': _list_includes})
        
        # Get libs and dependencies
        tree.deepTravers(_getLibraries, args = {'_list_libraries': _list_libraries})

        # Desactivate the output
        # TODO: esta linea debe cambiarse a MESSAGES_tools.output_deactivate() y su contraria MESSAGES_tools.output_activate()
        # para evitar que MESSAGES_tools.OUTPUT_ACTIVATED se asigne aun tipo no bool
        MESSAGES_tools.OUTPUT_ACTIVATED = True
        
        sourceCXX = self._getSource('source_cxx')
        sourceC = self._getSource('source_c')
        
        # create command of Basic
        Basic_t._generateCommand(
                dir                 = self.this_dir,
                builder_name        = self.build_name,
                name_out            = self.config_build.get("name_out")           if self.config_build.get("name_out")          != None else self.build_name,
                build_dir           = config_obj.get('build_dir'),
                type_project        = config_obj.get("type_project"),
                c_compiler          = self.config_build.get("c_compiler")           if self.config_build.get("c_compiler")          != None else 'gcc',
                cxx_compiler        = self.config_build.get("cxx_compiler")         if self.config_build.get("cxx_compiler")        != None else 'g++',
                linker              = self.config_build.get("linker")               if self.config_build.get("linker")              != None else 'g++',
                c_compiler_regex    = self.config_build.get("c_compiler_regex")     if self.config_build.get("c_compiler_regex")    != None else '$C -c $FILE -o $FILE_OUT',
                cxx_compiler_regex  = self.config_build.get("cxx_compiler_regex")   if self.config_build.get("cxx_compiler_regex")  != None else '$CXX -c $FILE -o $FILE_OUT',
                linker_regex        = self.config_build.get("linker_regex")         if self.config_build.get("linker_regex")        != None else '$LD $FILES -o $FILE_OUT',
                extension_files     = self.config_build.get("extension_files")      if self.config_build.get("extension_files" )    != None else ['.c', '.cc', '.cpp'],
                c_source            = sourceC,
                cxx_source          = sourceCXX,
                include_dirs        = list(set(include_local + _list_includes)),
                libs                = list(set(_list_libraries)),
            )

        MESSAGES_tools.OUTPUT_ACTIVATED = True
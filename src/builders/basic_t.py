######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 15/08/2022
### license = PSF
### version = 3.3.4 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
from distutils.command.build_ext import extension_name_re
import subprocess
import os
import platform

# Local Packages

from src.models.config_t import config_t as Config_t
import src.tool.messages as MESSAGES_tools
import src.funcs.includes as INCLUDE_funcs
import src.tool.string as STRING_tools
import src.tool.types as TYPES_tools
import src.tool.os as OS_tools
from src.models.tree_t import Tree_t as Tree_t
from src.models.tree_t import Dependencie_t as Dependencie_t

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
        type_project: str, 
        c_compiler: str, 
        cxx_compiler: str, 
        include_dirs: list,
        libs: list,
        c_source: list,
        cxx_source: list
        ):
        # TODO: Hacer un .sh para ejecutar la linea -> $CXX $FILE -o $FILE.o para cada archivo recivido en cxx_source
        return 'command basic'
    
    
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
                
                # Loop for sub files 
                for file in os.listdir(s_dir_path):
                    
                    # Complete path off File
                    s_file_path: str = s_dir_path + file
                    
                    # Check if s_file_path is a FIle and contains extension_files
                    if os.path.isfile(s_file_path) and s_file_path.find(extension_files) != -1:
                        
                        # Add File in source_list
                        source_list.append(s_file_path)
                    else:
                        
                        # Message(SuperWarning): OSError generate
                        MESSAGES_tools.message_error(s_file_path + ' Not is a File')
        return source_list
    
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
        
        print(sourceCXX)
        
        # create command of Cmake
        command = Basic_t._generateCommand(
                dir=self.this_dir,
                c_source=sourceC,
                cxx_source=sourceCXX,
                c_compiler=self.config_build["c_compiler"],
                cxx_compiler=self.config_build["cxx_compiler"],
                type_project=config_obj.get("type_project"),
                include_dirs=include_local + _list_includes,
                libs=_list_libraries
            )

        # Run the Cmake Command
        #subprocess.run(command)
        print(command)
        # Run the command of build system
        #subprocess.run(buildSystemCommand)


        MESSAGES_tools.OUTPUT_ACTIVATED = True
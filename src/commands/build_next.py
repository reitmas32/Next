######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 12/03/2022
### license = PSF
### version = 3.4.0
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
import os
import subprocess

#Local Packages
import src.funcs.read_config
import src.tool.messages as MESSAGES_tools
import src.models.build_t
import src.tool.os as OS_tools

def build(build_name=None):
    """Build project from current directory
    """
    
    try:
        
        # Current directory
        this_dir = os.getcwd()
        
        try:
            
            # Read config of proyect
            config_obj = src.funcs.read_config.read_config(this_dir)

            # If the configuration is not empty
            if config_obj != False:

                # Mkdir build_dir
                OS_tools.mkdirDir(config_obj.get('build_dir'))
                
                # Message(Waiting): Build Proyect
                MESSAGES_tools.message_waiting("Build Proyect")
                
                # Create a buider
                build_obj = src.models.build_t.Build_t(build_name, config_obj, this_dir)
                
                #Build the Builder
                build_obj.build()
                
            # The configuration is empty
            else:
                # Message(Warning): The configuration is empty
                MESSAGES_tools.message_warning("The configuration is empty")

        except OSError as exc:
            
            # Message(Error): OSError generate
            MESSAGES_tools.message_error(str(exc))
    except OSError as err:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(err))
        
        # Exit to program
        exit()
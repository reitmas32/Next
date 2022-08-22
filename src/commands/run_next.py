######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 20/03/2022
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

def run():
    """Run executable of project
    """

    # Get current directory
    this_dir = os.getcwd()
    
    try:
        
        #Read Config of Project
        config_obj = src.funcs.read_config.read_config(this_dir)

        # If this is a project of Next
        if config_obj != False:
            
            # Enter the directory bulid_dir
            os.chdir(config_obj.get("build_dir"))
            
            # Message(Waiting): Run executable
            MESSAGES_tools.message_waiting('Run executable')
            
            # Run executable
            subprocess.run(["./" + config_obj.get("name_build")])
    except OSError as exc:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
        # Exit to program
        exit()
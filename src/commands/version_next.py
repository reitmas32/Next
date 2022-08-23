######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 28/03/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Update 28/03/2022
VERSION = "3.4.0"

#System Packages
import os

#Local Packages
import src.funcs.read_config
import src.tool.messages as MESSAGES_tools


def version():
    # Message(Info): Next Version
    MESSAGES_tools.message_info("Next version: " + VERSION)

def version_all():
    
    # Next Packages Dierctory
    next_packages_dir = ""
    try:
        #Search NEXT_PACKAGES_DIR
        next_packages_dir = os.environ['NEXT_PACKAGES_DIR']
        
        # Message(Info): NEXT_PACKAGES_DIR in:
        MESSAGES_tools.message_info("NEXT_PACKAGES_DIR in: " +  next_packages_dir)

    except:
        # Message(Error): Not Find NEXT_PACKAGES_DIR
        MESSAGES_tools.message_error("It was not found ENV NEXT_PACKAGES_DIR in func --src.commands.version_next.version_all()--")
        exit()

    # Get Subdirectories 
    list_next_packages = os.listdir(next_packages_dir)

    for next_pakage_dir in list_next_packages:

        # Read COnfig for DIrectory
        config_obj = src.funcs.read_config.read_config(next_packages_dir+ "/" + next_pakage_dir)

        # If exists src.models.config_t
        if config_obj != False:
            
            # Message(Info): Get Version of Proects
            MESSAGES_tools.message_info(config_obj.name_project + " " + config_obj.version + "\n")
    
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

#Local Packages
import src.tool.messages as MESSAGES_tools

def check_env():
    """Check if it exists NEXT_PACKAGES_DIR
    """
    try:
        #Search NEXT_PACKAGES_DIR
        next_dir = os.environ['NEXT_PACKAGES_DIR']
        
        # Message(Info): Next_PACKAGES_DIR in
        MESSAGES_tools.message_info('NEXT_PACKAGES_DIR in: ' + next_dir)
    except:
        # Message(Warning): Not Find NEXT_PACKAGES_DIR
        MESSAGES_tools.message_warning("It was not found ENV NEXT_PACKAGES_DIR")

        #Want to create NEXT_PACKAGES_DIR
        MESSAGES_tools.message_info("Create NEXT_PACKAGES_DIR y/n: ")
        src.create_next_packages_dir_flag = input()

        #Create or Not NEXT_PACKAGES_DIR
        if src.create_next_packages_dir_flag == "y":

            #Select dir for NEXT_PACKAGES_DIR
            select_next_packages_dir()
        else:

            # Message(Warning): Is not created NEXT_PACKAGES_DIR
            MESSAGES_tools.message_warning("Warning!!! you must create NEXT_PACKAGES_DIR")
        exit()

def select_next_packages_dir():
    """Select dir for NEXT_PACKAGES_DIR
    """

    #Search home dir
    home_dir = os.environ['HOME']

    #Default dor for NEXT_PACKAGES_DIR
    next_packages_dir = home_dir + "/NextPackages"

    # Message(Info): Acept dir for NEXT_PACKAGES_DIR
    MESSAGES_tools.message_info("NEXT_PACKAGES_DIR will be created in: " + home_dir + " y/n:")
    next_packages_dir_flag = input()

    #Use default dor for NEXT_PACKAGES_DIR or not
    if next_packages_dir_flag == "y":

        #Create dir for NEXT_PACKAGES_DIR
        src.create_next_packages_dir(next_packages_dir)
    else:
        #Message(Info): Select dir for NEXT_PACKAGES_DIR
        MESSAGES_tools.message_info("Enter the route where you want NEXT_PACKAGES_DIR: ")
        next_packages_dir = input()

        #Create dir for NEXT_PACKAGES_DIR
        src.create_next_packages_dir(next_packages_dir + "/NextPackages")

def create_next_packages_dir(dir):
    """Create dir for NEXT_PACKAGES_DIR

    Args:
        dir (str): Direction of Next Packages
    """

    #verify that it does not exist dir for NEXT_PACKAGES_DIR
    if not os.path.isdir(dir):
        
        #Create dir for NEXT_PACKAGES_DIR
        os.mkdir(dir)

    # Message(Successful): Create NEXT_PACKAGES_DIR
    MESSAGES_tools.message_successful('Now add environment variable NEXT_PACKAGES_DIR='+ dir)

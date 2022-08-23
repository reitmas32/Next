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

#System Packages
import os
import shutil

#Local Packages
import src.tool.file as FILE_tools
import src.tool.messages as MESSAGES_tools

def create(name, build_dir, name_build, build_system_exe, c_compiler, cxx_compiler, build_system, type_project):

    # Get current Directory
    this_dir = os.getcwd()

    next_dir = ""
    try:
        #Search NEXT_PACKAGES_DIR
        next_dir = os.environ['NEXT_DIR']
        
        # Message(Info): NEXT_DIR find in 
        MESSAGES_tools.message_info('NEXT_DIR in: ' + next_dir)

    except:
        # Message(Error): Not Find NEXT_DIR
        MESSAGES_tools.message_error('It was not found ENV NEXT_DIR')  
        exit()

    # Message(Waiting): Create a proyect of next in
    MESSAGES_tools.message_waiting('Create a proyect of next in: ' + this_dir + '/' + name)
    try:
        # Default Type Proyect
        base_project = "empty_executable/"
        if(type_project):
            
            # If type is a Library
            if(type_project == "static_library" or type_project == "dynamic_library"):
                base_project = "empty_library/"

        # Create the dir
        os.mkdir(name)

        # Get nextEmptyProjectDir
        next_empty_project_dir = next_dir + "/assets/" + base_project

        # Copy the nextEmptyProjectDir in new project {name}
        shutil.copytree(next_empty_project_dir, name, dirs_exist_ok=True)

        # View the dir of new project {name}
        dir_new_project = os.getcwd() + "/" + name

        FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__name_project__", name)
        FILE_tools.remplace_in_file(dir_new_project + "/CMakeLists.txt", "__name_project__", name)

        if build_dir:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_dir__", build_dir)
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_dir__", "build")

        if name_build:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__name_build__", name_build)
            FILE_tools.remplace_in_file(dir_new_project + "/CMakeLists.txt", "__name_build__", name_build)
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__name_build__", "app")
            FILE_tools.remplace_in_file(dir_new_project + "/CMakeLists.txt", "__name_build__", "app")

        if build_system_exe and build_system:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_system_exe__", build_system_exe)
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_system__", build_system)
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_system_exe__", "ninja")
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__build_system__", "Ninja")

        if c_compiler:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__c_compiler__", c_compiler)
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__c_compiler__", "gcc")

        if cxx_compiler:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__cxx_compiler__", cxx_compiler)
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__cxx_compiler__", "g++")

        if type_project:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__type_project__", type_project)
                
        else:
            FILE_tools.remplace_in_file(dir_new_project + "/config.yaml", "__type_project__", "executable")
            
        # Message(Successful): Create a proyect of next in
        MESSAGES_tools.message_successful('Create a proyect of next in: ' + this_dir + '/' + name)

    except OSError as exc:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))

######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 22/07/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
from logging import exception
import os
import datetime

#Local Packages
import src.funcs.read_config
import src.tool.file as FILE_tools
import src.tool.messages as MESSAGES_tools
import src.funcs.write_config as WRITE_funcs
import src.tool.types as TYPES_tools

# Packages Dependencies
import ruamel.yaml.comments

def use_path(name_dependencie, library_dir):
    """Add library to this project from full path

    Args:
        library_dir (str): full path of library
    """
    
    # Get current Directory
    this_dir = os.getcwd()

    try:
        
        # Read config of proyect
        config_obj = src.funcs.read_config.read_config(this_dir)
        
        # Read config of library
        config_lib = src.funcs.read_config.read_config(library_dir)

        # Get dependencies
        dependencies = config_obj.get('dependencies')
        
        # Get time now
        time = datetime.datetime.now()
        
        # Get name_project of library
        name_project = str(config_lib.get('name_project'))
        
        # Find the name in current dependencies
        dependencies_list = []
        if type(dependencies) != TYPES_tools.nullType():
            dependencies_list =list(dependencies)
        else: 
            dependencies = {}
        
        if name_dependencie in dependencies_list:
            
            # Message(Warning): Dependency already exists
            MESSAGES_tools.message_warning('Dependency already exists: ' + name_dependencie)
            
            # Message(Info): Want to update the dependency
            MESSAGES_tools.message_info('Want to update the dependency y/n:')
            
            # Raed input
            res = input()
            
            if res != 'y':
                
                # Message(Error): Dependency already exists
                MESSAGES_tools.message_error('The dependency already exists and is not updated to solve the problem choose another name for the dependency and try again')
                
                # Generate exception
                exception('Dependency already exists')
        
        # Add new dependencie        
        dependencies[name_dependencie] = ruamel.yaml.comments.CommentedMap(
            {
                'name': name_project,
                'date': "%s/%s/%s" % (time.day, time.month, time.year), 
                'dir': library_dir
            }
        )
        
        # Set dependencies in config_obj
        config_obj.set('dependencies', dependencies)

        # Write the config_obj update
        WRITE_funcs.write_property(config_obj=config_obj, dir=this_dir)

    except OSError as exc:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
        # Exit to program
        exit()
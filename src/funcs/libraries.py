######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 12/07/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import src.funcs.read_config
import src.tool.messages as MESSAGES_tools
import src.tool.types as TYPES_tools

def get_library(route: str):
    
    library = ''
    
    try:
        
        # Read config of proyect
        config_obj = src.funcs.read_config.read_config(route)
        library_yaml = config_obj.get('library')
        type_library = type(library_yaml)
        if type_library != TYPES_tools.nullType():
            library = route + '/' + library_yaml
        
    except OSError as exc:
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
    return library
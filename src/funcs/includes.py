######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 02/06/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import src.funcs.read_config
import src.tool.messages as MESSAGES_tools
import src.tool.types as TYPES_tools

def get_includes(route: str):
    
    list_includes = []
    
    try:
        
        # Read config of proyect
        config_obj = src.funcs.read_config.read_config(route)
        includes = config_obj.get('include_dirs')
        type_include = type(includes)
        if type_include != TYPES_tools.nullType():
            for include in includes:
                list_includes.append(route + '/' + include)
                
            list_includes.append(route)
        
    except OSError as exc:
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
    return list_includes
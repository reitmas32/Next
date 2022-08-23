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

# Local Packages
import src.funcs.read_config
import src.tool.messages as MESSAGES_tools
import src.tool.types as TYPES_tools


def get_dependencies(route: str):
    
    list_dependencies = []
    
    try:
        
        # Read config of proyect
        config_obj = src.funcs.read_config.read_config(route)
        
        dependencies = config_obj.get('dependencies')
        
        if type(dependencies) != TYPES_tools.nullType():

            for name_include in dependencies:
                
                list_dependencies.append({name_include: dict(dependencies[name_include]) })

    except OSError as exc:
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
    return list_dependencies
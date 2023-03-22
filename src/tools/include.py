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

from src.domain.config_t import Config_t
from src.domain.types.dir_t import Dir_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.null_smart_t import NullSmart_t

def get_includes(route: Dir_t):
    
    list_includes = []
    
    try:
        
        # Read config of proyect
        config_obj = Config_t(route)
        includes = config_obj.get('include_dirs')
        type_include = type(includes)
        if type_include != NullSmart_t.type_is():
            for include in includes:
                list_includes.append(route.path() + '/' + include)
                
            list_includes.append(route.path())
        
    except OSError as exc:
        # Message(Error): OSError generate
        MH.message_error(str(exc))
        
    return list_includes
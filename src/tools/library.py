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

from src.domain.config_t import Config_t
from src.domain.types.dir_t import Dir_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.null_smart_t import NullSmart_t

def get_library(route: Dir_t):
    
    library = ''
    
    try:
        
        # Read config of proyect
        config_obj = Config_t(route)
        library_yaml = config_obj.get('library')
        type_library = type(library_yaml)
        if type_library != NullSmart_t.type_is():
            library = route.path() + '/' + library_yaml
        
    except OSError as exc:
        # Message(Error): OSError generate
        MH.message_error(str(exc))
        
    return library
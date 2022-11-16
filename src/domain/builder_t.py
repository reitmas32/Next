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

from src.domain.types.null_smart_t import NullSmart_t
from src.domain.config_t import Config_t
from src.domain.types.dir_t import Dir_t
from src.ports.messages.message_handler import Message_Handler as MH

class Build_i:
    config_obj: Config_t  = NullSmart_t()
    this_dir = ""
    build_name = ""

    def __init__(self, build_name: str, config_obj: Config_t, this_dir: Dir_t):
        """Initialize a src.models.Build_t

        Args:
            build_name (str): Name of Build
            config_obj (Config_t)
            this_dir (Dir_t)
        """
        
        # Save the config_obj
        self.config_obj = config_obj
        
        # The directory
        self.this_dir = this_dir

        # The Name of Build
        self.build_name = build_name
                
    def build(self):
        pass
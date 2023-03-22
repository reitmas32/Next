######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 31/10/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

from src.domain.config_t import Config_t
from src.domain.types.dir_t import Dir_t
from src.ports.yaml.yaml_ruamel import yaml_ruamel_port
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e

from src.ports.yaml.yaml_ruamel import yaml_ruamel_port

import src.tools.file as FILE_TOOL

class Project_t:

    config: Config_t
    path: Dir_t

    def __init__(self, path: Dir_t = Dir_t('') ) -> None:
        self.path = path
        self.config = Config_t(self.path, yaml_port=yaml_ruamel_port())

    def write_config(self) -> StatusCode_t:

        try:
                    
            # Write Config
            with open('config.yaml', 'w') as file:
                #documents = self.config.yaml.dump(config_map, file)
                y = yaml_ruamel_port()
                s = y.object_to_yaml_str(self.config._data)
                file.write(s)
            
            # Remplace chars '[' and ']'
            FILE_TOOL.remplace_in_file("config.yaml", "'[", "[")
            FILE_TOOL.remplace_in_file("config.yaml", "]'", "]")
            
            return StatusCodes_e.SUCCESSFUL
        except:
            return StatusCodes_e.ERROR
        
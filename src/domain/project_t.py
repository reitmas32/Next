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

class Project_t:

    config: Config_t
    path: Dir_t

    def __init__(self, path: Dir_t = Dir_t('') ) -> None:
        pass
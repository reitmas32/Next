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

from src.domain.project_t import Project_t
from src.domain.types.dir_t import Dir_t
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e

class Builder_i:

    def __init__(self):
        """Initialize a src.models.Build_t

        Args:
            build_name (str): Name of Build
            config_obj (Config_t)
            this_dir (Dir_t)
        """
        pass

    def create_project(
        self, 
        next_dir:Dir_t, 
        this_dir:Dir_t,
        name_project:str
    )-> StatusCode_t:
        pass

    def create_project_api(
        self, 
        next_dir:Dir_t, 
        this_dir:Dir_t,
        name_project:str,
        data: dict
    )-> StatusCode_t:
        pass

    def create(
        self, 
        project: Project_t,
    )-> StatusCode_t:
        pass

    def create_api(
        self, 
        project: Project_t,
        data: dict
    )-> StatusCode_t:
        pass
                
    def build(self, project: Project_t, name_build: str)-> StatusCode_t:
        pass

    def build_api(self, project: Project_t, name_build: str)-> StatusCode_t:
        pass
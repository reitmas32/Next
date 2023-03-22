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

from typing import Any
from src.domain.types.null_smart_t import NullSmart_t

class yaml_interface:
    def __init__(self) -> None:
        pass

    def object_to_yaml_str(self, obj: Any, options=None) -> str:
        pass

    def yaml_string_to_object(self, string: str, options=None) -> object:
        pass

    # f->o
    def yaml_file_to_object(self, file_path: str, options=None) -> object:
        pass

    # o->f
    def object_to_yaml_file(self, obj: Any, file_path: str, options=None) -> object:
        pass
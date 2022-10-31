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

class yaml_interface:
    def __init__(self) -> None:
        pass

    def object_to_yaml_str(obj, options=None) -> str:
        pass

    def yaml_string_to_object(string, options=None) -> object:
        pass

    # f->o
    def yaml_file_to_object(file_path, options=None) -> object:
        pass

    # o->f
    def object_to_yaml_file(obj, file_path, options=None) -> object:
        pass
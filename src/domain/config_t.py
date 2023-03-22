######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 3/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Packages Dependencies

from typing import Any
from src.ports.yaml.yaml_interface import yaml_interface
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.dir_t import Dir_t, TypesDirs_e
from src.domain.types.null_smart_t import NullSmart_t

# Local Packages
#import src.tools.string as String_Tool

class Config_t:

    _data = {}
    file_path: Dir_t
    yaml = ''
    dir: Dir_t
    global_yaml_port: yaml_interface

    def __init__(self, dir: Dir_t, yaml_port: yaml_interface = NullSmart_t()):
        """Initialize a src.models.config_t

        Args:
            dir (str): Direction of project
        """
        self.dir = dir

        #Create dir of file_path 'config.yaml'
        self.file_path = Dir_t(dir.path() + "/config.yaml")

        #Read Data and load in self._data
        if self.file_path.exist and self.file_path.type_dir() == TypesDirs_e.FILE:
            if type(yaml_port) != NullSmart_t.type_is():
                self._data = yaml_port.yaml_file_to_object(file_path=self.file_path.path())
            else:
                self._data = Config_t.global_yaml_port.yaml_file_to_object(file_path=self.file_path.path())
            MH.message_successful('Read config of: ' + dir.path() )
        else:
            #TODO: Crear el Port de Messages
            MH.message_error('The address: ' + self.file_path.path() + ' does not exist or is not a file')
        pass

    def get(self, property: str) -> Any:
        """Get the property

        Args:
            property (_type_): Name of Property

        Returns:
            str: Value of property
        """
        try:
            value = self._data[property]
            if value == None:
                value = NullSmart_t()
        except:
            value = NullSmart_t()
        return value

    def set(self, property: str, value: Any) -> Any:
        """Set the property

        Args:
            property (str): Name of property
            value (obj_yaml): Value of property

        Returns:
            obj_yaml: Value of property
        """
        try:
            self._data[property] = value
            new_value = self._data[property]
        except:
            MH.message_error('Property does not exist')
            new_value = NullSmart_t()
        return new_value

    def add(self, property: str, value: Any) -> Any:
        """Set the property

        Args:
            property (str): Name of property
            value (obj_yaml): Value of property

        Returns:
            obj_yaml: Value of property
        """
        try:
            self._data[property] = value
            new_value = self._data[property]
        except:
            MH.message_error("Property does not exist")
            new_value = NullSmart_t()
        return new_value

    def to_map(self) -> dict:
        """Convert src.models.config_t to Map

        Returns:
            Map: Map of Data
        """
        return self._data
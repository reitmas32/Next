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

from src.ports.yaml.yaml_interface import yaml_interface
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.dir_t import Dir_t, TypesDirs_e

# Local Packages
#import src.tools.string as String_Tool

class Config_t:

    _data = {}
    file_path: Dir_t
    yaml = ''

    def __init__(self, dir: Dir_t, yaml_port: yaml_interface):
        """Initialize a src.models.config_t

        Args:
            dir (str): Direction of project
        """

        #Create dir of file_path 'config.yaml'
        self.file_path = Dir_t(dir.path() + "/config.yaml")

        #Read Data and load in self._data
        if self.file_path.exist and self.file_path.type_dir() == TypesDirs_e.FILE:
            self._data = yaml_port.yaml_file_to_object(file_path=self.file_path.path())
            MH.message_successful('Read config of: ' + dir.path() )
        else:
            #TODO: Crear el Port de Messages
            MH.message_error('The address: ' + self.file_path.path() + ' does not exist or is not a file')
        pass

    def get(self, property):
        """Get the property

        Args:
            property (_type_): Name of Property

        Returns:
            str: Value of property
        """
        pass

    def set(self, property, value):
        """Set the property

        Args:
            property (str): Name of property
            value (obj_yaml): Value of property

        Returns:
            obj_yaml: Value of property
        """
        pass

    def add(self, property, value):
        """Set the property

        Args:
            property (str): Name of property
            value (obj_yaml): Value of property

        Returns:
            obj_yaml: Value of property
        """
        pass

    def to_map(self):
        """Convert src.models.config_t to Map

        Returns:
            Map: Map of Data
        """
        pass
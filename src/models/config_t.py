######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 20/03/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Packages Dependencies
import ruamel.yaml

# Packges Local
import src.tool.messages as MESSAGES_tools
import src.tool.yaml as YAML_tools
import src.tool.types as TYPES_tools

def listToString(l):
    """Convert a list to a string

    Args:
        l (list): List to convert

    Returns:
        str: string
    """
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(l))

class config_t:

    _data = {}
    file = ''
    yaml = ''

    def __init__(self, dir):
        """Initialize a src.models.config_t

        Args:
            dir (str): Direction of project
        """
        # Create a Yaml
        self.yaml = ruamel.yaml.YAML()
        self.yaml.preserve_quotes = True

        #Read file
        self.file = dir + "/config.yaml"

        #Write Data
        #self._data = self.yaml.load(self.file)
        self._data = YAML_tools.yaml_file_to_object(self.file)

    def print(self):
        """Print the src.models.config_t
        """
        print( "name_project: "         + self._data["name_project"])
        print( "description: "          + self._data["description"])
        print( "version: "              + self._data["version"])
        print( "build_dir: "            + self._data["build_dir"])
        print( "name_build: "           + self._data["name_build"])
        print( "build_system_exe: "     + self._data["build_system_exe"])
        print( "c_compiler: "           + self._data["c_compiler"])
        print( "cxx_compiler: "         + self._data["cxx_compiler"])
        print( "build_system: "         + self._data["build_system"])
        print( "cmake_flags: "          + listToString(self._data["cmake_flags"]))
        print( "build_system_flags: "   + listToString(self._data["build_system_flags"]))

    def get(self, property):
        """Get the property

        Args:
            property (_type_): Name of Property

        Returns:
            str: Value of property
        """
        try:
            value = self._data[property]
            if value == None:
                value = TYPES_tools.NullType()
        except:
            value = TYPES_tools.NullType()
        return value

    def set(self, property, value):
        """Set the property

        Args:
            property (str): Name of property
            value (obj_yaml): Value of property

        Returns:
            obj_yaml: Value of property
        """
        try:
            current_value = self._data[property]
            self._data[property] = value
            new_value = self._data[property]
        except:
            MESSAGES_tools.message_error("Property does not exist")
            new_value = TYPES_tools.NullType()
        return new_value

    def add(self, property, value):
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
            MESSAGES_tools.message_error("Property does not exist")
            new_value = TYPES_tools.NullType()
        return new_value

    def to_map(self):
        """Convert src.models.config_t to Map

        Returns:
            Map: Map of Data
        """
        return self._data
######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 13/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

from src.domain.command_i import Command_i
from src.domain.project_t import Project_t
from src.domain.types.null_smart_t import NullSmart_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.ports.yaml.yaml_ruamel import yaml_ruamel_port
from src.domain.types.status_code_t import StatusCodes_e, StatusCode_t
import src.tools.string as String_Tool


class GetCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self, property: str, comments: bool = True) -> StatusCode_t:

        # default value of property
        value_of_property = "null"

        # alone Next version
        if(property != ""):

            #Wrapper for properties
            value_of_property = self.project.config.get(property)
            
            #If it was added correctly
            if(type(value_of_property) != NullSmart_t.type_is()):

                yaml_port = yaml_ruamel_port()
                
                value_of_property_str = yaml_port.object_to_yaml_str(value_of_property).replace("...", "")
                
                if comments == False:
                    value_of_property_str = String_Tool.stripComments(value_of_property_str)
                # Message(Successful): Getting property
                MH.message_successful('Getting property \n' + property + ': ' +  value_of_property_str)
                
            else:
                # Message(Error): Could not add
                MH.message_error('Could not get ' + property)
                return StatusCodes_e.ERROR

        #Value of new property ([str, null])
        return StatusCodes_e.SUCCESSFUL
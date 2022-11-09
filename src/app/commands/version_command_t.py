######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 28/03/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Update 28/03/2022
VERSION = "3.4.0"

#System Packages
import os

#Local Packages
from src.ports.messages.message_handler import Message_Handler as MH

from src.domain.command_i import Command_i
from src.domain.types.status_code_t import StatusCodes_e

class VersionCommand_t(Command_i):

    def __init__(self) -> None:
        super().__init__()

    def exec(self):
        
        MH.message_info("Next version: " + VERSION)
        return StatusCodes_e.SUCCESSFUL
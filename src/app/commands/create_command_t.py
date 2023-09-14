######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 06/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import os
from src.domain.types.dir_t import Dir_t

from src.domain.command_i import Command_i
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e

from src.app.builders.builders import base_builders

import config as CONFIG

class CreateCommand_t(Command_i):

    def __init__(self) -> None:
        super().__init__()

    def exec(self, name_project: str, base_build: str):
        # Get current Directory
        this_dir = os.getcwd()

        next_dir = ""
        try:
            #Search NEXT_PACKAGES_DIR
            next_dir = CONFIG.NEXT_DIR
            
            # Message(Info): NEXT_DIR find in 
            MH.message_info('NEXT_DIR in: ' + next_dir)

            try:
                builder = base_builders[base_build]
                builder.create_project(next_dir=Dir_t(next_dir), this_dir=Dir_t(this_dir), name_project= name_project)
            except Exception as e:
                MH.message_error('Base Project Undefind')
                print(e)
                return StatusCodes_e.ERROR
            
        except Exception as e:
            # Message(Error): Not Find NEXT_DIR
            MH.message_error('It was not found ENV NEXT_DIR')
            print(e)
            return StatusCodes_e.ERROR

        return StatusCodes_e.SUCCESSFUL
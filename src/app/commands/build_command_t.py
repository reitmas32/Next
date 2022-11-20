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

from src.domain.command_i import Command_i
from src.domain.project_t import Project_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e

from src.app.builders.builders import base_builders


class BuildCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self, name_build: str):

        next_dir = ""
        try:
            #Search NEXT_PACKAGES_DIR
            next_dir = os.environ['NEXT_DIR']
            
            # Message(Info): NEXT_DIR find in 
            MH.message_info('NEXT_DIR in: ' + next_dir)

            try:
                #TODO: this is the most insecure thing i have ever done repair asap
                base_build = self.project.config.get('builds')[name_build]['base']
                builder = base_builders[base_build]
                builder.build(project=self.project, name_build=name_build)
            except Exception as e:
                MH.message_error('Base Project Undefind in build_command')
                print(e)  
            
        except:
            # Message(Error): Not Find NEXT_DIR
            MH.message_error('It was not found ENV NEXT_DIR')  
            exit()

        return StatusCodes_e.SUCCESSFUL
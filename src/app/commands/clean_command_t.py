######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 14/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

import shutil
import platform

from src.domain.command_i import Command_i
from src.domain.project_t import Project_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e

# Open script of bash
SYSTEM = platform.system()


_SLASH_CHAR = '/'

if SYSTEM != 'Linux':
    _SLASH_CHAR = '\\'



class CleanCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self, name_build: str):


        try:
            if name_build == 'all':

                name_build = ''

                # Remove the directory "build_dir"
                shutil.rmtree(self.project.config.get("build_dir"))
                
                # Message(Successful): The build_dir delete
                MH.message_successful('Clean ' + self.project.path.path() + _SLASH_CHAR + self.project.config.get("build_dir"))
            else:
                # Remove the directory "build_dir"
                shutil.rmtree(self.project.config.get("build_dir") + _SLASH_CHAR + name_build)
                
                # Message(Successful): The build_dir delete
                MH.message_successful('Clean Build: ' + self.project.path.path() + _SLASH_CHAR + self.project.config.get("build_dir") + _SLASH_CHAR + name_build)
        except Exception as e:
            MH.message_error('Could Not Delete: ' + self.project.config.get("build_dir") + _SLASH_CHAR + name_build)
            MH.message_error(str(e))  

        return StatusCodes_e.SUCCESSFUL
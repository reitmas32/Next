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
import shutil

from src.domain.project_t import Project_t
from src.domain.command_i import Command_i
from src.app.funcs.print_tree import printTree
from src.domain.types.dir_t import Dir_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e


class TreeCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self):
        try:
            printTree(dir=self.project.path)
        except:
            MH.message_error('Cold not Print Tree of: ' + self.project.path.path())
        return StatusCodes_e.SUCCESSFUL
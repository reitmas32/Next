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


from src.domain.command_i import Command_i
from src.domain.project_t import Project_t
from src.domain.types.dir_t import TypesDirs_e
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e
from src.domain.types.dir_t import Dir_t

from src.app.commands.set_command_t import SetCommand_t



class ExportCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self, library: str):


        try:
            lib_dir = Dir_t(library)
            if lib_dir.type_dir() == TypesDirs_e.FILE:
                _set = SetCommand_t(self.project)
                _set.exec('library', library)
                MH.message_successful('Add Export library: ' + self.project.path.path() + '/' + library)
            elif lib_dir.type_dir() == TypesDirs_e.DIR:
                MH.message_error('library property is not a file: ' + self.project.path.path() + '/' + library)
                return StatusCodes_e.ERROR
            else:
                MH.message_error('library property does not exist: ' + self.project.path.path() + '/' + library)
                return StatusCodes_e.ERROR
        except Exception as e:
            MH.message_error('library property does not exist: ' + self.project.path.path() + '/' + library)
            return StatusCodes_e.ERROR

        return StatusCodes_e.SUCCESSFUL
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

#System Packages
import os

#Local Packages
import src.tools.os as OS_TOOLS
from src.ports.messages.message_handler import Message_Handler as MH

from src.domain.command_i import Command_i
from src.domain.types.status_code_t import StatusCodes_e

from src.domain.types.dir_t import Dir_t, TypesDirs_e

#External Packages
from git import Repo

"""
How Use this Command
> next install -g https://github.com/reitmas32/Moon.git

--------
Pasos
- Verificar que este instalado Git ✓
- Verificar que exista $NEXT_PACKAGES_DIR ✓
- clonar el repositorio en el Directorio $NEXT_PACKAGES_DIR ✓

- Revisar las dependencias del Packages e instalarlas ×

"""


class InstallCommand_t(Command_i):

    def __init__(self) -> None:
        super().__init__()

    def exec(self, url, name_packages):
        # Git Check
        git_scripts = OS_TOOLS.find_script_on_path('git', _equal= True)
        git_version_output = b''
        if len(git_scripts) < 1:
            # Message(Error): OSError generate
            MH.message_error('Not Git Installed on your System')
            
            return StatusCodes_e.ERROR
        
        next_packages_dir = None
        #NEXT_PACKAGES_DIR Check
        try:
            next_packages_dir = Dir_t(os.environ['NEXT_PACKAGES_DIR'])
            
            if next_packages_dir.type_dir() == TypesDirs_e.NONE:
                # Message(Error): OSError generate
                MH.message_error('$NEXT_PACKAGES_DIR dir not exist')
                
                return StatusCodes_e.ERROR
            
        except Exception as e:
            # Message(Waiting): The dir folder already exists

            MH.message_warning("$NEXT_PACKAGES_DIR environment variable does not exist: " + str(e))
            
        # Clone Repo
        Repo.clone_from(url, f"{next_packages_dir.path()}/{name_packages}")
            
        
        return StatusCodes_e.SUCCESSFUL
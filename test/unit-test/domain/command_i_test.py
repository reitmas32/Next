######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 31/10/2022
### license = PSF
### version = 3.4.0 
### test_files = src/domain/command_i.py
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Testing
######################################################################


from domain.project_t import Project_t
from domain.types.status_code_t import StatusCode_t, StatusCodes_e
from src.domain.command_i import Command_i

def simple_command_test():

    class Echo_Command(Command_i):
        def __init__(self) -> None:
            Command_i.__init__(self)

    echo = Echo_Command()

    assert echo.exec() == StatusCodes_e.SUCCESSFUL

def override_exec_test():

    class Error_Command(Command_i):
        def __init__(self) -> None:
            Command_i.__init__(self)

        def exec(project: Project_t) -> StatusCode_t:
            return StatusCodes_e.ERROR

    echo = Error_Command()

    assert echo.exec() == StatusCodes_e.ERROR


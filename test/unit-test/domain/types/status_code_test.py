######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 31/10/2022
### license = PSF
### version = 3.4.0 
### test_files = src/domain/types/status_code.py
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Testing
######################################################################

from domain.types.status_code_t import StatusCode_t, StatusCodes_e
from src.domain.command_i import Command_i

def successful_code_test():

    assert StatusCodes_e.SUCCESSFUL == StatusCode_t(0, 'SUCCESSFUL')

def error_code_test():

    assert StatusCodes_e.ERROR == StatusCode_t(-1, 'ERROR')
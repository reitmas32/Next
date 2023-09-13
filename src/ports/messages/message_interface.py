######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 03/10/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Packages Systems
from typing import Tuple
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e


class message_handdler_i:
    def __init__(self) -> None:
        pass

    def message_error(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.ERROR
        
    def message_warning(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.WARNING
        
    def message_successful(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.SUCCESSFUL
        
    def message_info(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.SUCCESSFUL
        
    def message_waiting(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.SUCCESSFUL

    def message_question(messageQuestion: str) -> Tuple[StatusCode_t, object]:
        return StatusCodes_e.SUCCESSFUL, True
    
    def message_unknown(messageStr: str) -> StatusCode_t:
        return StatusCodes_e.ERROR
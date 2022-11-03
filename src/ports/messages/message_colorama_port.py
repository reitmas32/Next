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
import platform
from src.ports.messages.message_interface import message_handdler_i
from src.domain.types.status_code_t import StatusCode_t, StatusCodes_e

# Packages Dependencies
from colorama  import Fore
from colorama import Style
import colorama

class _message_handdler_colorama_port(message_handdler_i):

    OUTPUT_ACTIVATED = True

    def __init__(self) -> None:
        # For colorama in Windows load ANSI
        system = platform.system()
        if system != 'Linux':
            colorama.init(convert = True)
        pass

    def message_error(self, messageStr: str) -> StatusCode_t:
        print(f'{Fore.RED}{Style.BRIGHT} <<ERROR>> {Style.RESET_ALL}' + messageStr)
        return StatusCodes_e.ERROR
        
    def message_warning(self, messageStr: str) -> StatusCode_t:
        if self.OUTPUT_ACTIVATED == True : print(f'{Fore.YELLOW}{Style.BRIGHT} <<WARNING>> {Style.RESET_ALL}' + messageStr)
        return StatusCodes_e.WARNING
        
    def message_successful(self, messageStr: str) -> StatusCode_t:
        if self.OUTPUT_ACTIVATED == True : print(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT} <<SUCCESSFUL>> {Style.RESET_ALL}' + messageStr)
        return StatusCodes_e.SUCCESSFUL
        
    def message_info(self, messageStr: str) -> StatusCode_t:
        if self.OUTPUT_ACTIVATED == True : print(f'{Fore.WHITE}{Style.BRIGHT} <<INFO>> {Style.RESET_ALL}' + messageStr)
        return StatusCodes_e.SUCCESSFUL
        
    def message_waiting(self, messageStr: str) -> StatusCode_t:
        if self.OUTPUT_ACTIVATED == True : print(f'{Fore.BLUE}{Style.BRIGHT} <<WAITING...>> {Style.RESET_ALL}' + messageStr)
        return StatusCodes_e.SUCCESSFUL

Message_Handler_Colorama_Port = _message_handdler_colorama_port()
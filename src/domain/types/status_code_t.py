######################################################################
# author = Rafael Zamora
# copyright = Copyright 2020-2022, Next Project
# date = 30/10/2022
### license = PSF
# version = 3.4.0
# maintainer = Rafael Zamora
### email = rafa.zamora.ram@gmail.com
### status = Production
######################################################################

class StatusCode_t:
    _code: int
    _lable: str

    def __init__(self, code: int, lable: str) -> None:
        self._code = code
        self._lable = lable
        pass

    def __str__(self) -> str:
        return '{ ' + str(self._code) + ', ' + self._lable + ' }'

    def string(self) -> str:
        return 'StatusCode: ' + self._code + ', Lable: ' + self._lable 


class StatusCodes_e:
    SUCCESSFUL = StatusCode_t(0, 'SUCCESSFUL')
    ERROR = StatusCode_t(-1, 'ERROR')

######################################################################
### author = Rafael Zamora
### copyright = Copyright 2020-2022, Next Project
### date = 30/10/2022
### license = PSF
### version = 3.4.0
### maintainer = Rafael Zamora
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

    def __eq__(self, __o: object) -> bool:
        if self.code() == __o.code():
            return True
        return False

    def string(self) -> str:
        return 'StatusCode: ' + str(self._code) + ', Lable: ' + self._lable 

    def code(self) -> int:
        return self._code


class StatusCodes_e:
    SUCCESSFUL = StatusCode_t(0, 'SUCCESSFUL')
    ERROR = StatusCode_t(-1, 'ERROR')
    WARNING = StatusCode_t(1, 'WARNING')

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

# System Packages
import os

from src.ports.messages.message_handler import Message_Handler as MH
#TODO: Documetar las calse y la enum 
class _TypeDir_t:
    _type_dir = int
    _lable: str

    def __init__(self, type_dir: int, lable: str) -> None:
        self._type_dir = type_dir
        self._lable = lable

    def __str__(self) -> str:
        return '{ ' + str(self._type_dir) + ', ' + self._lable + ' }'

    def __eq__(self, __o: object) -> bool:
        if self.type_dir() == __o.type_dir():
            return True
        return False

    def type_dir(self) -> int: 
        return self._type_dir

    def string(self) -> str:
        return 'TypeDir: ' + self._lable


class TypesDirs_e:
    FILE = _TypeDir_t(0, 'FILE')
    DIR = _TypeDir_t(1, 'DIR')
    LINK = _TypeDir_t(2, 'LINK')
    NONE = _TypeDir_t(-1, 'NONE')


class Dir_t:
    _type_dir: _TypeDir_t
    _path: str
    _exists: bool = False

    def __init__(self, path: str) -> None:
        try: 
            self._path = path
            if os.path.exists(self._path):
                self._exists = True

                if os.path.isdir(self.path()):
                    self._type_dir = TypesDirs_e.DIR

                if os.path.isfile(self.path()):
                    self._type_dir = TypesDirs_e.FILE

                if os.path.islink(self.path()):
                    self._type_dir = TypesDirs_e.LINK
            else:
                self._exists = False
                self._type_dir = TypesDirs_e.NONE
        except Exception as e:
            MH.message_error( str(e))

    def __str__(self) -> str:
        return '{ ' + self.path() + ', ' + str(self.type_dir()) + ', ' + str(self.exist()) + ' }'

    def __eq__(self, __o: object) -> bool:
        if self.path() == __o.path():
            return True
        return False
    
    def string(self) -> str:
        return 'Path: ' + self.path() + ', TypeDir: ' + str(self.type_dir()) + ', Exist: ' + str(self.exist())

    def path(self) -> str:
        return self._path

    def type_dir(self) -> _TypeDir_t:
        return self._type_dir

    def exist(self) -> bool:
        return self._exists

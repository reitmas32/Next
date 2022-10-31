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

# System Packages
import os


class _TypeDir_t:
    _type_dir = str
    _lable: str

    def __init__(self, type_dir: str, lable: str) -> None:
        self._type_dir = type_dir
        self._lable = lable

    def __str__(self) -> str:
        return '{ ' + str(self._type_dir) + ', ' + self._lable + ' }'

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

    def __str__(self) -> str:
        return '{ ' + self.path() + ', ' + str(self.type_dir()) + ', ' + str(self.exist()) + ' }'

    def string(self) -> str:
        return 'Path: ' + self.path() + ', TypeDir: ' + str(self.type_dir()) + ', Exist: ' + str(self.exist())

    def path(self) -> str:
        return self._path

    def type_dir(self) -> str:
        return self._type_dir

    def exist(self) -> bool:
        return self._exists

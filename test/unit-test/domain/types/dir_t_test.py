######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 31/10/2022
### license = PSF
### version = 3.4.0 
### test_files = src/domain/types/dit_t.py
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Testing
######################################################################

from domain.types.dir_t import Dir_t, TypesDirs_e

def dir_t_exist_test():

    setup = Dir_t('setup.py')

    assert setup.exist() == True

def dir_t_type_test():

    setup = Dir_t('setup.py')

    assert setup.type_dir() == TypesDirs_e.FILE

def dir_t_equal_test():

    setup = Dir_t('setup.py')
    setup_copy = Dir_t('setup.py')

    assert setup == setup_copy
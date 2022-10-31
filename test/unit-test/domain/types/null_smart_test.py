######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 31/10/2022
### license = PSF
### version = 3.4.0 
### test_files = src/domain/types/null_smart.py
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Testing
######################################################################

from domain.types.null_smart_t import NullSmart_t

def null_smart_test():

    assert type(NullSmart_t()) == NullSmart_t.type_is()
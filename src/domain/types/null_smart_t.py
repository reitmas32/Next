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

class NullSmart_t:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return 'NullSmart_t'
    
    def type_is() -> type:
        """Retrurn Type of NullSmart_t

        Returns:
            type: Type of NullSmart_t
        """
        return type(NullSmart_t())
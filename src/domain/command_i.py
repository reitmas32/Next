######################################################################
### author = Rafael Zamora
### copyright = Copyright 2020-2022, Next Project
### date = 31/10/2022
### license = PSF
### version = 3.4.0
### maintainer = Rafael Zamora
### email = rafa.zamora.ram@gmail.com
### status = Production
######################################################################


from src.domain.project_t import Project_t
from src.domain.types.status_code_t import StatusCodes_e, StatusCode_t


class Command_i:
    def __init__(self) -> None:
        pass

    def exec(self, project: Project_t) -> StatusCode_t:
        return StatusCodes_e.SUCCESSFUL

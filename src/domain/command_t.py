from src.domain.project_t import Project_t
from src.domain.types.status_code_t import StatusCodes, StatusCode_t

class Command_t:
    def __init__(self) -> None:
        pass

    def exec(project: Project_t) -> StatusCode_t:
        return StatusCodes.SUCCESFUL
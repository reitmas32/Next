######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 14/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################


import datetime
from logging import exception
from src.domain.command_i import Command_i
from src.domain.project_t import Project_t
from src.domain.types.dir_t import TypesDirs_e
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.status_code_t import StatusCodes_e
from src.domain.types.dir_t import Dir_t
from src.domain.types.null_smart_t import NullSmart_t

from src.app.commands.set_command_t import SetCommand_t

# Packages Dependencies
#TODO: Hcer port de esto
import ruamel.yaml.comments

class ImportCommand_t(Command_i):

    project: Project_t

    def __init__(self, project: Project_t) -> None:
        self.project = project
        Command_i.__init__(project)

    def exec(self, name_library: str , dir_library: str):


        try:
            lib_dir = Dir_t(dir_library)
            if lib_dir.type_dir() == TypesDirs_e.DIR:
                
                library_project = Project_t(lib_dir)
                
                # Get dependencies
                dependencies = self.project.config.get('dependencies')
        
                # Get time now
                time = datetime.datetime.now()
        
                # Get name_project of library
                name_library_project = library_project.config.get('name_project')
                
                dependencies_list = []
                if type(dependencies) != NullSmart_t.type_is():
                    dependencies_list = list(dependencies)
                else: 
                    dependencies = {}

                if name_library in dependencies_list:
                    
                    # Message(Warning): Dependency already exists
                    MH.message_warning('Dependency already exists: ' + name_library)
                    
                    # Raed input
                    _, res=MH.message_question('Want to update the dependency {y|n}: ', defaultAnswer='n', printDefault=True, listAnswer=['y', 'n'])
                    
                    if res != 'y':
                        
                        # Message(Error): Dependency already exists
                        MH.message_error('The dependency already exists and is not updated to solve the problem choose another name for the dependency and try again')
                        
                        # Generate exception
                        return StatusCodes_e.ERROR


                # Add new dependencie
                # TODO: Hacer port de esto    
                dependencies[name_library] = ruamel.yaml.comments.CommentedMap(
                    {
                        'name': name_library_project,
                        'date': "%s/%s/%s" % (time.day, time.month, time.year), 
                        'dir': dir_library
                    }
                )
                
                # Set dependencies in config_obj
                self.project.config.set('dependencies', dependencies)

                self.project.write_config()
                
                MH.message_successful('Add Export library: ' + self.project.path.path() + '/' + dir_library)
            elif lib_dir.type_dir() == TypesDirs_e.FILE:
                MH.message_error('dir_library property is not a dir: ' + self.project.path.path() + '/' + dir_library)
                return StatusCodes_e.ERROR
            else:
                MH.message_error('dir_library property does not exist: ' + self.project.path.path() + '/' + dir_library)
                return StatusCodes_e.ERROR
        except Exception as e:
            MH.message_error('library property does not exist: ' + self.project.path.path() + '/' + dir_library)
            return StatusCodes_e.ERROR

        return StatusCodes_e.SUCCESSFUL
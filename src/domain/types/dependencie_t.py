######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 3/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

from src.domain.types.dir_t import Dir_t
from src.domain.types.null_smart_t import NullSmart_t
from src.domain.config_t import Config_t
from src.ports.messages.message_handler import Message_Handler as MH

import src.tools.include as INCLUDE_TOOL
import src.tools.library as LIBRARY_TOOL


#TODO: Ducumentar la classe por lo demas se ve bien
class Dependencie_t:
    name: str
    dir: Dir_t
    date: str
    num_deep:int = 0
    includes = []
    library: str
    def __init__(self, data: dict, num_deep: int) -> None:
        self.name = ''
        self.dir = ''
        self.date = ''
        self.num_deep = num_deep
        for x in data.keys():
            if x == 'name':
                self.name = data['name']
            elif x == 'dir':
                self.dir = Dir_t(data['dir'])
            elif x == 'date':
                self.date = data['date']
        
        self.includes = INCLUDE_TOOL.get_includes(self.dir)
        self.library = LIBRARY_TOOL.get_library(self.dir)
        
    
    def __str__(self):
        return 'Name: ' + self.name + ', Dir: ' + self.dir.path() + ', Date: ' + self.date

    def get_dependencies(route: Dir_t):
    
        list_dependencies = []
        
        try:
            
            # Read config of proyect
            config_obj = Config_t(route)
            
            dependencies = config_obj.get('dependencies')
            
            if type(dependencies) != NullSmart_t.type_is():

                for name_include in dependencies:
                    
                    list_dependencies.append({name_include: dict(dependencies[name_include]) })

        except OSError as exc:
            # Message(Error): OSError generate
            MH.message_error(str(exc))
            
        return list_dependencies

    
    def print(self):
        side_shift = '    ' * self.num_deep
        # print
        print(side_shift + '' + '-----------------------------------------')
        print(side_shift + '|' + self.name + ':')
        print(side_shift + '|' + '  ' + 'name: ' + self.name)
        print(side_shift + '|' + '  ' + 'date: ' + self.date)
        print(side_shift + '|' + '  ' + 'dir: '  + self.dir.path())
        print(side_shift + '' + '-----------------------------------------')
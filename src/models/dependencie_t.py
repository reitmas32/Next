import src.funcs.includes as INCLUDE_funcs
import src.funcs.libraries as LIBRARIES_funcs

class Dependencie_t:
    name: str
    dir: str
    date: str
    num_deep:int = 0
    include = []
    library: str
    def __init__(self, data: dict, num_deep = 0) -> None:
        self.name = ''
        self.dir = ''
        self.date = ''
        self.num_deep = num_deep
        for x in data.keys():
            if x == 'name':
                self.name = data['name']
            elif x == 'dir':
                self.dir = data['dir']
            elif x == 'date':
                self.date = data['date']
        
        self.include = INCLUDE_funcs.get_includes(self.dir)
        self.library = LIBRARIES_funcs.get_library(self.dir)
        
    
    def __str__(self):
        return 'Name: ' + self.name + ', Dir: ' + self.dir + ', Date: ' + self.date
    
    def print(self):
        side_shift = '    ' * self.num_deep
        # print
        print(side_shift + '' + '-----------------------------------------')
        print(side_shift + '|' + self.name + ':')
        print(side_shift + '|' + '  ' + 'name: ' + self.name)
        print(side_shift + '|' + '  ' + 'date: ' + self.date)
        print(side_shift + '|' + '  ' + 'dir: '  + self.dir)
        print(side_shift + '' + '-----------------------------------------')
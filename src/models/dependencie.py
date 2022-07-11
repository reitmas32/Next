class Dependencie_t:
    name: str
    dir: str
    date: str
    def __init__(self, data: dict) -> None:
        self.name = ''
        self.dir = ''
        self.date = ''
        for x in data.keys():
            if x == 'name':
                self.name = data['name']
            elif x == 'dir':
                self.dir = data['dir']
            elif x == 'date':
                self.date = data['date']
        pass
    
    def __str__(self):
        return 'Name: ' + self.name + ', Dir: ' + self.dir + ', Date: ' + self.date
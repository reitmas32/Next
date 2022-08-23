######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 02/06/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

class Node_t:
    
    data = None
    childs = []
    
    def __init__(self, data):
        self.data = data
        self.childs = []

    def __str__(self):
        return 'Node: ' + str(self.data)
        
    def new_child(self,child):
        self.childs.append(child)
        
    def lenChilds(self):
        return self.childs.count()

    def deepTravers(self, func, args:dict, num_deep = 0):
        func(self.data, num_deep, args=args)
        if len(self.childs) > 0:
            for c in self.childs:
                c.deepTravers(func, num_deep = num_deep + 1, args = args)

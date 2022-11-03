######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 03/10/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

from typing import Generic, TypeVar

T = TypeVar('T')

class Node_t(Generic[T]):
    
    data = None
    childs: list[T]
    
    def __init__(self, data: T):
        self.data = data
        self.childs = []

    def __str__(self):
        return 'Node: ' + str(self.data)
        
    def new_child(self,child: object):
        self.childs.append(child)
        
    def lenChilds(self):
        return len(self.childs)

    def deepTravers(self, func, args:dict, num_deep = 0):
        func(self.data, num_deep, args=args)
        if len(self.childs) > 0:
            for c in self.childs:
                c.deepTravers(func, num_deep = num_deep + 1, args = args)
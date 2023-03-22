######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 22/07/2022
### license = PSF
### version = 3.4.0
### maintainer = Rafael Zamora
### email = rafa.zamora.ram@gmail.com 
### status = Development
######################################################################

# Local Packages
from src.domain.types.dir_t import Dir_t
from src.domain.types.dependencie_t import Dependencie_t
from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.tree_t import Tree_t


def printDependencie(dependencie: Dependencie_t, num_deep: int , args:dict):
    side_shift = '   ' * num_deep
    format = args['format']
    if format == True:
        dependencie.print()
    else:
        print(side_shift + str(dependencie))

def printTree(dir:Dir_t):
    """Print the tree of current directory
    """
    
    try:
        
        # Desactivate output of messages
        MH.OUTPUT_ACTIVATED = False
        
        # Get the of current project
        tree = Tree_t(dir)

        tree.deepTravers(printDependencie, args = {'format': True})
        
        # Activate output of messages
        MH.OUTPUT_ACTIVATED = True

    except OSError as err:
        
        # Message(Error): OSError generate
        MH.message_error(str(err))
        
        # Exit to program
        exit()
        
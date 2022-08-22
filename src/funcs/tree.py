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
from src.models.dependencie_t import Dependencie_t
import src.tool.messages as MESSAGES_tools
from src.models.tree_t import Tree_t as Tree_t


def printDependencie(dependencie: Dependencie_t, num_deep: int , args:dict):
    side_shift = '   ' * num_deep
    format = args['format']
    if format == True:
        dependencie.print()
    else:
        print(side_shift + str(dependencie))

def printTree(dir = ''):
    """Print the tree of current directory
    """
    
    try:
        
        # Desactivate output of messages
        MESSAGES_tools.OUTPUT_ACTIVATED = False
        
        # Get the of current project
        tree = Tree_t(dir)

        tree.deepTravers(printDependencie, args = {'format': True})
        
        # Activate output of messages
        MESSAGES_tools.OUTPUT_ACTIVATED = True

    except OSError as err:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(err))
        
        # Exit to program
        exit()
        
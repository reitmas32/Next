######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 05/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# System Packages
import datetime 

# Local Packages
from src.domain.types.dependencie_t import Dependencie_t
from src.domain.types.dir_t import Dir_t
from src.domain.config_t import Config_t
import src.tools.json as JSON_TOOLS
from src.ports.messages.message_handler import Message_Handler as MH
#import src.tool.json as JSON_tools
from src.domain.types.node_t import Node_t

from src.ports.yaml.yaml_ruamel import yaml_ruamel_port

class Tree_t:
    root: Node_t
    
    def __init__(self, root_dir: Dir_t):
        """Function of activation Recursive
        """
        
        # The Tree empty
        self.root = None
        
        try:
            
            # Desactivate output of messages
            MH.OUTPUT_ACTIVATED = True
            
            # Get the configuration of project
            config_obj: Config_t = Config_t(root_dir, yaml_ruamel_port())
            
            # Get the tree
            self.root = Tree_t.TreeDependencies(
                config_obj.get('name_project'), 
                {
                    'type': config_obj.get('type_project'),
                    'dir': root_dir.path()
                } , 
                0)
            
        except OSError as err:
            
            # Message(Error): OSError generate
            MH.message_error(str(err))
            
            # Exit to program
            exit()
            
    def TreeDependencies(key_dependencie: str, value_dependencie: dict, num_deep: int):
        """Recursive func for getting dependencies

        Args:
            key_dependencie (str): The name of dependencie
            value_dependencie (dict): The map of data of dependencie
            num_deep (int): deep of tree
            stdout (bool): Flag for activate the output
        """
        
        # Create the new Node
        if num_deep == 0:
            e = datetime.datetime.now()
            value_dependencie['name'] = key_dependencie
            value_dependencie['date'] = "%s/%s/%s" % (e.day, e.month, e.year)
        
        tree = Node_t(Dependencie_t( value_dependencie, num_deep = num_deep))
        
        # Get dependencies of current node
        dependencies = Dependencie_t.get_dependencies(Dir_t(value_dependencie['dir']))
        
        # Verify if exists dependencies
        if(len(dependencies) >= 1):
        
            # iter all dependencies
            for dep in dependencies:
                
                # Get data
                key = JSON_TOOLS.jsonObjKey(dep)
                value = JSON_TOOLS.jsonObjValue(dep)
                
                # Continue with the Tree
                tree.new_child(Tree_t.TreeDependencies(key, value, num_deep + 1))

        return tree
            
    def deepTravers(self, func, args:dict, num_deep = 0):
        self.root.deepTravers(func, args=args, num_deep=num_deep)
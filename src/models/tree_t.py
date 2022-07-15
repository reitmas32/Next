# System Packages
import datetime 

# Local Packages
from src.models.dependencie_t import Dependencie_t
from src.models.config_t import config_t as Config_t
import src.funcs.includes
import src.funcs.dependencies
import src.tool.messages as MESSAGES_tools
import src.tool.json as JSON_tools
from src.models.node_t import Node_t as Node_t

class Tree_t:
    root: Node_t
    
    def __init__(self, root_dir):
        """Function of activation Recursive
        """
        
        # The Tree empty
        self.root = None
        
        try:
            
            # Desactivate output of messages
            MESSAGES_tools.OUTPUT_ACTIVATED = False
            
            # Get the configuration of project
            config_obj: Config_t = src.funcs.read_config.read_config(root_dir)
            
            # Get the tree
            self.root = Tree_t.TreeDependencies(
                config_obj.get('name_project'), 
                {
                    'type': config_obj.get('type_project'),
                    'dir': root_dir
                } , 
                0)
            
        except OSError as err:
            
            # Message(Error): OSError generate
            MESSAGES_tools.message_error(str(err))
            
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
        dependencies = src.funcs.dependencies.get_dependencies(value_dependencie['dir'])
        
        # Verify if exists dependencies
        if(len(dependencies) >= 1):
        
            # iter all dependencies
            for dep in dependencies:
                
                # Get data
                key = JSON_tools.jsonObjKey(dep)
                value = JSON_tools.jsonObjValue(dep)
                
                # Continue with the Tree
                tree.new_child(Tree_t.TreeDependencies(key, value, num_deep + 1))

        return tree
            
    def deepTravers(self, func, args:dict, num_deep = 0):
        self.root.deepTravers(func, args=args, num_deep=num_deep)
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

import src.tool.messages as MESSAGES_tools
import os

def mkdirDir(dir:str):
    
    try:
        # Try create build_dir
        os.mkdir(dir)
        
        # Message(Successful): The dir directory was created
        MESSAGES_tools.message_successful('MKDIR : ' + dir)
        
    except:
        # Message(Waiting): The dir folder already exists
        MESSAGES_tools.message_warning("Warning " + dir +  " folder already exists")
                
def find_files_for_ext(dir: str, ext = '.py'):
    files_with_ext = []
    
    # Iter files rcursive
    for path, currentDirectory, files in os.walk(dir):
        
        # Added files to list
        files_with_ext += [os.path.join(path, f) for f in files if f.endswith(ext)]
    
    # Return files
    return files_with_ext
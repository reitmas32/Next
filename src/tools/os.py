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

from src.ports.messages.message_handler import Message_Handler as MH
from src.domain.types.dir_t import Dir_t
import os

def mkdirDir(dir:Dir_t):
    
    try:
        # Try create build_dir
        os.mkdir(dir.path())
        
        # Message(Successful): The dir directory was created
        MH.message_successful('MKDIR : ' + dir.path())
        
    except Exception as e:
        # Message(Waiting): The dir folder already exists

        MH.message_warning("Warning " + str(dir) +  " folder already exists -> " + str(e))

def makeDirs(dir:Dir_t):
    
    try:
        # Try create build_dir
        os.makedirs(dir.path())
        
        # Message(Successful): The dir directory was created
        MH.message_successful('MKDIR : ' + dir.path())
        
    except Exception as e:
        # Message(Waiting): The dir folder already exists

        MH.message_warning("Warning " + str(dir) +  " folder already exists -> " + str(e))
                
def find_files_for_ext(dir: str, ext = '.py'):
    files_with_ext = []
    
    # Iter files rcursive
    for path, currentDirectory, files in os.walk(dir):
        
        # Added files to list
        files_with_ext += [os.path.join(path, f) for f in files if f.endswith(ext)]
    
    # Return files
    return files_with_ext

def find_script_on_path(script_tag: str, full_path=False, _start = True, _max_results=10, _equal = False) -> list[str]:
    match_scripts = []
    for dir in os.environ['PATH'].split(':'):
        for script in os.listdir(dir):
            if len(match_scripts) >= _max_results:
                return match_scripts
            if _equal:
                if script_tag == script:
                    match_scripts.append(f"{dir}/{script}") if full_path else match_scripts.append(f"{script}")
            else:
                if script.find(script_tag) != -1:
                    if _start:
                        if script.find(script_tag) == 0:
                            match_scripts.append(f"{dir}/{script}") if full_path else match_scripts.append(f"{script}")
                    else:
                        match_scripts.append(f"{dir}/{script}") if full_path else match_scripts.append(f"{script}")
    return match_scripts
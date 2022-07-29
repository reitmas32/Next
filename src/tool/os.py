######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 02/06/2022
### license = PSF
### version = 3.3.4 
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
                
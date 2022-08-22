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

# Packages Systems
import os
import platform

# Packages Dependencies
import ruamel.yaml

def load_env():
    """load the environment variables in the current execution
    """
    try:
        env_yaml = ''
        
        file = ''
        
        _data = {}
        
        #Get Home Dir
        system = platform.system()
        
        if system == 'Linux':
            print('Linux System')
            home_dir = os.environ['HOME']
        else:
            print('Windows System')
            home_dir = os.environ['LOCALAPPDATA']
        
        next_env_file_dir = home_dir + '/.next/env.yaml'
        
        env_yaml = ruamel.yaml.YAML()
        
        env_yaml.preserve_quotes = True

        #Read the file
        file = open( next_env_file_dir, "r")

        #Safe the data
        _data = env_yaml.load(file)
        
        #Load the environment variables in the current execution
        for x in _data:
            print(x + '= ' + _data[x])
            os.environ[x] = _data[x]
        
    except:
        
        print("Error at Load Env")
######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 29/03/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

#System Packages
import os
import subprocess

#Local Packages
import src.funcs.read_config
import src.tool.messages as MESSAGES_tools

def exce(command):
    """Execute a command
    """
    
    # Get current Directory
    this_dir = os.getcwd()
    try:
        
        # Read config of proyect
        config_obj = src.funcs.read_config.read_config(this_dir)

        # If the configuration is not empty
        if config_obj != False:
            
            try:
                #Get Commands
                commands = config_obj.get('commands')

                # Get keys
                keys_commands = commands.keys()
                
                # Value of Command 
                value_command = ''
                
                # Flag
                find = False
                
                # Search command
                for x in keys_commands:
                    
                    # Find Command
                    if x == command :
                        
                        # Set Flag
                        find = True
                        
                        # Save value of command
                        value_command = commands[command]
                        
                        # Break the Search
                        break
                
                # If Find the Command
                if( find ):
                    
                    # Message(Waiting): Executing the command
                    MESSAGES_tools.message_waiting('Executing the command: ' + command)
                    subprocess.run(list(value_command.split(" ")))
                else: 
                    # Message(Error): Executing the command
                    MESSAGES_tools.message_error('Command not found: ' + command)
                
            except OSError as err:
                # Message(Error): OSError generate
                MESSAGES_tools.message_error(str(err))
    except OSError as exc:
        
        # Message(Error): OSError generate
        MESSAGES_tools.message_error(str(exc))
        
        # Exit to program
        exit()
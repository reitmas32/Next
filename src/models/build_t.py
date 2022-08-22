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

import src.models.config_t
import src.builders.cmake_t
import src.builders.basic_t
import src.tool.messages as MESSAGES_tools

class Build_t:
    
    builder = None
    config_build = {}
    config_obj = None
    this_dir = ""
    build_name = ""

    def __init__(self, build_name, config_obj: src.models.config_t.config_t, this_dir):
        """Initialize a src.models.Build_t

        Args:
            build_name (str): Name of Build
            config_obj (src.models.Config_t)
        """
        
        # Save the config_obj
        self.config_obj = config_obj
        
        # The directory
        self.this_dir = this_dir

        # The Name of Build
        self.build_name = build_name
        
        # Get Builds
        builds = config_obj.get('builds')

        # Check that it is not None
        if build_name != None:
            
            # Select the Builder
            self._select_builder(build_name, builds)
        else:
            
            # Setup if no name explicit
            self._none_name()
            
    def _select_builder(self, build_name: str, builds):
        """ Select a Build

        Args:
            build_name (str): Name of Build
            builds (list: {}): List of Builds
        """
        # Try get Build 
        try:
            
            #Find Build
            self.config_build = builds[build_name]
        
            # Selctor of base of Build
            if self.config_build['base'] == 'cmake':
                self.builder = src.builders.cmake_t.Cmake_t(self.config_build, self.this_dir, self.build_name)
            if self.config_build['base'] == 'basic':
                self.builder = src.builders.basic_t.Basic_t(self.config_build, self.this_dir, self.build_name)
        except KeyError as exc:
            
            # Message(Error): OSError generate
            MESSAGES_tools.message_error('The name of the requested build does not exist: ' + str(exc))
                
    def _none_name(self):
        """Initialize a src.models.Build_t without build_name explicit
        """
        
        # Get a Builds
        builds = self.config_obj.get('builds')
        
        if builds != None:
            
            # Get a first builder
            for builder in builds:
                self.build_name = builder
                self._select_builder(builder, builds)
                break
        else:
            # Message(Error): OSError generate
            MESSAGES_tools.message_error('There are no builds to be able to build the project')
                
    def build(self):
        
        # check that it is not None
        if self.builder != None:
            
            # Call to Build
            self.builder.build(self.config_obj)
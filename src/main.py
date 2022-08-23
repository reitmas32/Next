######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 29/01/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Packages Dependencies
from email.policy import default
import click

#Local Packages
import src.commands.info_next as Info_Next
import src.commands.version_next as Version_Next
import src.commands.create_next as Create_Next
import src.commands.build_next as Build_Next
import src.commands.run_next as Run_Next
import src.commands.clean_next as Clean_Next
import src.commands.config_env as Config_Env
import src.commands.config_get as Config_Get
import src.commands.config_set as Config_Set
import src.commands.config_add as Config_Add
import src.tool.env as ENV_tools
import src.commands.exce_next as Exce_Next
import src.commands.use_next as Use_Next
import src.funcs.tree as Tree_funcs
import src.tool.types as TYPES_tools

# Packages System
import os

### Update 22/07/2022
### ✓ create                   Create a new Next project.
### ✓ build                    Build this project
### ✓ run                      Run your app
### ✓ clean                    Remove the binaries
### ✓ version                  List Next and plugins version.
### ✓ info                     Print Info verbose of Next
### ✓ add                      Add to property of current Next Project
### ✓ get                      Get to property of current Next Project
### ✓ set                      Set to property of current Next Project
### ✓ exce                     Excecute a command perzonalized
### ✓ import                   Import a new library
### ✓ tree                     Get the tree of current project
### ✓ export                   Export the library .a .so .lib .dll

### × remove                   Remove a library
### × install                  Install a Plugin
### × upgrade                  Upgrade a Plugin or Next
### × doctor                   Show information about the installed tooling.

@click.group()
def main():
    ENV_tools.load_env()
    pass

@main.command('info', short_help='view info the Next')
def info():
    Info_Next.info()

@main.command('version', short_help='view version the Next')
@click.option('--all',default=0, required=False, help='view version of all NextPackages installed <default=0>')
def version(all: int):
    # alone Next version
    if(all == 0):
        Version_Next.version()
    # all NextPackages
    elif(all == 1):
        Version_Next.version_all()
    # Error Not show any version
    else:
        exit()

@main.command('check_env', short_help='check env the NextPackages')
def check_env():
    Config_Env.check_env()

@main.command('create', short_help='Create a new project of Next', options_metavar='<name> <options>')
@click.argument('name', required=True, type=str, metavar='')
@click.option('--build_dir', required=False, type=str, help='Select Build Dir', default='build')
@click.option('--name_build', required=False, type=str, help='Select name of build', default='app')
@click.option('--build_system_exe', required=False, type=str, help='Select Build System executable')
@click.option('--c_compiler', required=False, type=str, help='Select C Compiler')
@click.option('--cxx_compiler', required=False, type=str, help='Select C++ Compiler')
@click.option('--build_system', required=False, type=str, help='Select Build System')
@click.option('--type_project', required=False, type=str, help='Select Type Project', default='executable')
def create(
    name: str, 
    build_dir: str, 
    name_build: str, 
    build_system_exe: str, 
    c_compiler: str, 
    cxx_compiler: str, 
    build_system: str, 
    type_project: str
    ):
    Create_Next.create(name, build_dir, name_build, build_system_exe, c_compiler, cxx_compiler, build_system, type_project)

@main.command('build', short_help='Build a project of Next')
@click.argument('build_name', default=None, required=False, type=str, metavar='')
def build(build_name: str):
    Build_Next.build(build_name)

@main.command('run', short_help='Run a project of Next')
def run():
    Run_Next.run()

@main.command('clean', short_help='Clean a project of Next')
def clean():
    Clean_Next.clean()

@main.command('get', short_help='Get property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--comments',default=True, required=False, type=bool, help='Select name of build')
def get(property: str, comments: bool):
    value_of_property = Config_Get.get(property, comments)

@main.command('set', short_help='Set property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--value',default="name", required=True, help='Select value of current Next Project <default=null>')
def set(property: str, value):
    Config_Set.set(property, value)

@main.command('add', short_help='Add to property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--value',default="name", required=True, help='Select value of current Next Project <default=null>')
def add(property: str, value):
    Config_Add.add(property, value)
    
@main.command('exec', short_help='Excecute a coomand of Project of property <commands>')
@click.argument('command')
def exce(command: str):
    Exce_Next.exce(command)
    
@main.command('import', short_help='Add new library in current project')
@click.argument('name_dependencie')
@click.option('--dir', required=True, type=str, help='Select Dir of dependencie')
def import_command(name_dependencie: str, dir: str):
    Use_Next.use_path(name_dependencie, dir)

@main.command('tree', short_help='Run a project of Next')
def tree():
    this_dir = os.getcwd()

    Tree_funcs.printTree(dir=this_dir)
    
@main.command('export', short_help='Export library of current project')
@click.argument('library', required=True, type=str, metavar='libraryPath')
def export(library):
    if type(Config_Set.set('library', library)) == TYPES_tools.nullType():
        Config_Add.add('library', library)
    
#if __name__ == "__main__":
#main()

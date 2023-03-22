######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2022, Next Project 
### date = 14/11/2022
### license = PSF
### version = 3.4.0 
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

# Packages Dependencies
import click

#Tools

#Types
from src.domain.config_t import Config_t
from src.domain.types.dir_t import Dir_t
from src.domain.project_t import Project_t
from src.app.commands.get_command_t import GetCommand_t
from src.app.commands.set_command_t import SetCommand_t
from src.app.commands.add_command_t import AddCommand_t

#Commands
from src.app.commands.build_command_t import BuildCommand_t
from src.app.commands.info_command_t import InfoCommand_t
from src.app.commands.create_command_t import CreateCommand_t
from src.app.commands.version_command_t import VersionCommand_t
from src.app.commands.clean_command_t import CleanCommand_t
from src.app.commands.export_command_t import ExportCommand_t
from src.app.commands.import_command_t import ImportCommand_t
from src.app.commands.tree_command_t import TreeCommand_t
from src.app.commands.doctor_command_t import DoctorCommand_t

#Ports
from src.ports.yaml.yaml_ruamel import yaml_ruamel_port

# Packages System
import os

### Update 14/11/2022
### ✓ create                   Create a new Next project.
### ✓ build                    Build this project
### × run                      Run your app
### ✓ clean                    Remove the binaries
### ✓ version                  List Next and plugins version.
### ✓ info                     Print Info verbose of Next
### ✓ add                      Add to property of current Next Project
### ✓ get                      Get to property of current Next Project
### ✓ set                      Set to property of current Next Project
### × exce                     Excecute a command perzonalized
### ✓ import                   Import a new library
### ✓ tree                     Get the tree of current project
### ✓ export                   Export the library .a .so .lib .dll

### × remove                   Remove a library
### × install                  Install a Plugin
### × upgrade                  Upgrade a Plugin or Next
### × doctor                   Show information about the installed tooling.

#Middelwares
Config_t.global_yaml_port = yaml_ruamel_port()

THIS_DIR = os.getcwd()

@click.group()
def main():
    pass

@main.command('info', short_help='view info the Next')
def info():
    i = InfoCommand_t()
    i.exec()

@main.command('version', short_help='view version the Next')
@click.option('--all',default=0, required=False, help='view version of all NextPackages installed <default=0>')
def version(all: int):
    v = VersionCommand_t()
    v.exec()

@main.command('check_env', short_help='check env the NextPackages')
def check_env():
    print('check-env')

@main.command('create', short_help='Create a new project of Next', options_metavar='<name> <options>')
@click.argument('name', required=True, type=str, metavar='')
@click.option('--base', required=False, type=str, help='Select Base Builder', default='basic')
def create(
    name: str, 
    base: str
    ):

    c = CreateCommand_t()
    c.exec(name, base)

@main.command('build', short_help='Build a project of Next')
@click.argument('name_build', default=None, required=False, type=str, metavar='')
def build(name_build: str):

    b = BuildCommand_t(Project_t(Dir_t(THIS_DIR)))

    b.exec( name_build=name_build)

@main.command('run', short_help='Run a project of Next')
def run():
    print('Run')

@main.command('clean', short_help='Clean a project of Next')
@click.argument('name_build', default='all', required=False, type=str, metavar='')
def clean(name_build: str):
    c = CleanCommand_t(project=Project_t(Dir_t(THIS_DIR)))

    c.exec(name_build)

@main.command('get', short_help='Get property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--comments',default=True, required=False, type=bool, help='Select name of build')
def get(property: str, comments: bool):
    _get = GetCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    _get.exec(property)

@main.command('set', short_help='Set property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--value',default="name", required=True, help='Select value of current Next Project <default=null>')
def set(property: str, value):
    _set = SetCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    _set.exec(property, value)

@main.command('add', short_help='Add to property of current Next Project')
@click.argument('property', required=True, type=str, metavar='property')
@click.option('--value',default="name", required=True, help='Select value of current Next Project <default=null>')
def add(property: str, value):
    _add = AddCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    _add.exec(property, value)
    
@main.command('exec', short_help='Excecute a coomand of Project of property <commands>')
@click.argument('command')
def exce(command: str):
    print('Exec')
    
@main.command('import', short_help='Add new library in current project')
@click.argument('name_library')
@click.option('--dir', required=True, type=str, help='Select Dir of dependencie')
def import_command(name_library: str , dir: str):
    i = ImportCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    i.exec(name_library, dir)

@main.command('tree', short_help='Run a project of Next')
def tree():
    t = TreeCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    t.exec()
    
@main.command('export', short_help='Export library of current project')
@click.argument('library', required=True, type=str, metavar='libraryPath')
def export(library):
    e = ExportCommand_t(project=Project_t(Dir_t(THIS_DIR)))
    e.exec(library)

@main.command('doctor', short_help='view doctor the Next')
def doctor():
    v = DoctorCommand_t()
    v.exec()
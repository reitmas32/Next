######################################################################
### author = Rafael Zamora 
### copyright = Copyright 2020-2023, Next Project 
### date = 22/03/2023
### license = PSF
### version = 3.5.0
### maintainer = Rafael Zamora 
### email = rafa.zamora.ram@gmail.com 
### status = Production
######################################################################

from src.domain.command_i import Command_i
from src.domain.types.status_code_t import StatusCodes_e

import src.tools.string as STRING_TOOL

import os
import subprocess
INSTALLED = f'✓'
NOT_INSTALLED = f'×'

"""


> next doctor

[✓] C++ Compilers and Tools: g++, clang++, cl
[✓] C Compilers and Tools: gcc, clang, cl
[✓] Git : git version 2.34.1
[✓] Cmake : <<Cmake version output>>

--------------New Version------------ :TODO
[✓] Ninja : <<Ninja version output>>
[✓] Gradle : <<Ninja version output>>
[✓] Premake : <<Ninja version output>>
"""


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

class DoctorCommand_t(Command_i):

    def __init__(self) -> None:
        super().__init__()

    def exec(self):
        
        # C/C++ Compilers and Tools
        gcc_compilers_and_tools = find_script_on_path('gcc')
        clang_compilers_and_tools = find_script_on_path('clang')
        cl_compilers_and_tools = find_script_on_path('cl', _equal= True)
        
        c_compilers_and_tools = STRING_TOOL.listToStr(set(gcc_compilers_and_tools + clang_compilers_and_tools + cl_compilers_and_tools), separator=', ')
        
        gxx_compilers_and_tools = find_script_on_path('g++')
        clangxx_compilers_and_tools = find_script_on_path('clang++')
        
        cxx_compilers_and_tools = STRING_TOOL.listToStr(set(gxx_compilers_and_tools + clangxx_compilers_and_tools + cl_compilers_and_tools), separator=', ')
        
        # Git
        git_scripts = find_script_on_path('git', _equal= True)
        git_version_output = b''
        if len(git_scripts) >= 1:
            git_version_output = subprocess.run(['git', '--version'], capture_output=True).stdout
            
        # Cmake
        cmake_scripts = find_script_on_path('cmake', _equal= True)
        cmake_version_output = b''
        if len(cmake_scripts) >= 1:
            cmake_version_output = subprocess.run(['cmake', '--version'], capture_output=True).stdout
        
        print(f"[{INSTALLED if len(c_compilers_and_tools) >= 1 else NOT_INSTALLED}] C Compilers and Tools: {c_compilers_and_tools}")
        print(f"[{INSTALLED if len(cxx_compilers_and_tools) >= 1 else NOT_INSTALLED}] C++ Compilers and Tools: {cxx_compilers_and_tools}")
        print(f"[{INSTALLED if git_version_output != b'' else NOT_INSTALLED}] Git: {git_version_output.decode()}")
        print(f"[{INSTALLED if cmake_version_output != b'' else NOT_INSTALLED}] CMake: {cmake_version_output.decode()}")
        return StatusCodes_e.SUCCESSFUL
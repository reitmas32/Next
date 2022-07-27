---
title: First Project
description: How Create a first Project
layout: ../../../layouts/MainLayout.astro
---

This section will talk about how to create a first project with Next and how buiild the app

##### **Create the project**

```bash
next create first_project
```

OutPut

```bash
Linux System
NEXT_DIR= /home/user/Next
NEXT_PACKAGES_DIR= /home/user/Next_Packages
 <<INFO>> NEXT_DIR in: /home/user/Next
 <<WAITING...>> Create a proyect of next in: /home/user/documents/first_project
 <<SUCCESSFUL>> Create a proyect of next in: /home/user/documents/first_project

```

##### **Struct of Project**

```
.
├── cmake
│   ├── linux.cmake
│   ├── vendor.cmake
│   └── windows.cmake
├── CMakeLists.txt
├── config.yaml
└── src
    └── main.cpp

```

The cmake folder will be explained in more detail in the [builder Cmake](https://www.next-project.com/builders/cmake)

The more import is a *config.yaml* file

##### **Show the config.yaml**

```yaml
name_project: first_project
type_project: executable
description: Hello World in Moon
version: v0.0.1
build_dir: build
include_dirs:
- include
dependencies:
  # hello_world:
  #   name: Name
  #   date: 19/07/2022
  #   dir: dir_of__dependencie
name_build: app
builds:
  cmake_release:
    base: cmake
    build_system_exe: make
    c_compiler: gcc
    cxx_compiler: g++
    build_system: Unix Makefiles
    cmake_flags: []
    build_system_flags: []
commands:
  src: cd src
#  test: g++ test/test.cpp -o build/test
#  run-test: ./build/test
```

##### **Build the project**

```bash
next build
```

OutPut

```bash
Linux System
NEXT_DIR= /home/user/Next
NEXT_PACKAGES_DIR= /home/user/Next_Packages
 <<SUCCESSFUL>> /home/user/documents/first_project Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/first_project
 <<SUCCESSFUL>> /home/user/documents/first_project Is a project of Next
 <<SUCCESSFUL>> MKDIR : build
 <<WAITING...>> Build Proyect
 <<SUCCESSFUL>> MKDIR : cmake_release
 <<SUCCESSFUL>> /home/user/documents/first_project Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/first_project
 <<SUCCESSFUL>> /home/user/documents/first_project Is a project of Next
-- The CXX compiler identification is GNU 11.2.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    CMAKE_C_COMPILER


-- Build files have been written to: /home/user/documents/first_project/build/cmake_release
[ 50%] Building CXX object CMakeFiles/app.dir/src/main.cpp.o
[100%] Linking CXX executable app
[100%] Built target app
```

##### **Run the app**

```bash
./build/cmake_release/app
```

OutPut

```bash
Hello World with Next
```
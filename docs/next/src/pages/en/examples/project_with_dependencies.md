---
title: Project with Dependencies
description: How Create a first Project
layout: ../../../layouts/MainLayout.astro
---

This section will talk about how to import a library with Next and how buiild the app

**We will use the [first_project](/en/get_started/first_project)**

##### Added dependencie

```bash
next import my_lib --dir /home/user/documents/basic_library
```

OutPut

```bash
Linux System
NEXT_DIR= /home/user/Next
NEXT_PACKAGES_DIR= /home/user/Next_Packages
 <<SUCCESSFUL>> /home/user/documents/first_project Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/first_project
 <<SUCCESSFUL>> /home/user/documents/first_project Is a project of Next
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/basic_library
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a project of Next
 <<SUCCESSFUL>> /home/user/documents/first_project Is a directory
```

##### Using the libarary

New src/main.cpp

```c
//  src/main.cpp

#include <iostream>
#include <hello_world.hpp>

int main(int argc, char const *argv[])
{
    std::cout << "Hello World with Next" << std::endl;
    hello_world();
    return 0;
}
```

##### Build the app

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
 <<WARNING>> Warning build folder already exists
 <<WAITING...>> Build Proyect
 <<WARNING>> Warning cmake_release folder already exists
 <<SUCCESSFUL>> /home/user/documents/first_project Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/first_project
 <<SUCCESSFUL>> /home/user/documents/first_project Is a project of Next
-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/documents/first_project/build/cmake_release
```
---
title: Basic Library
description: How Create a Libarary with Next
layout: ../../../layouts/MainLayout.astro
---

This section will talk about how to create a basic library with Next and how buiild the library

##### **Create the project**

```bash
next create basic_library --type_project static_library
```

OutPut

```bash
Linux System
NEXT_DIR= /home/user/Next
NEXT_PACKAGES_DIR= /home/user/Next_Packages
 <<INFO>> NEXT_DIR in: /home/user/Next
 <<WAITING...>> Create a proyect of next in: /home/user/documents/basic_library
 <<SUCCESSFUL>> Create a proyect of next in: /home/user/documents/basic_library
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
├── include
│   └── hello_world.hpp
└── src
    └── hello_world.cpp
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
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/basic_library
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a project of Next
 <<SUCCESSFUL>> MKDIR : build
 <<WAITING...>> Build Proyect
 <<SUCCESSFUL>> MKDIR : cmake_release
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/basic_library
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a project of Next
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


-- Build files have been written to: /home/user/documents/basic_library/build/cmake_release
[ 50%] Building CXX object CMakeFiles/app.dir/src/hello_world.cpp.o
[100%] Linking CXX static library libapp.a
[100%] Built target app
```

##### **Export library**

```bash
next export build/cmake_release/libapp.a
```

OutPut

```bash
Linux System
NEXT_DIR= /home/user/Next
NEXT_PACKAGES_DIR= /home/user/Next_Packages
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a directory
 <<SUCCESSFUL>> Exists config.yaml in :/home/user/documents/basic_library
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a project of Next
 <<SUCCESSFUL>> /home/user/documents/basic_library Is a directory
 <<SUCCESSFUL>> Set property library: build/cmake_release/libapp.a
```
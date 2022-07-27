---
title: Config.yaml Basic
description: Description of config.yaml file
layout: ../../../layouts/MainLayout.astro
---

In the config.yaml file you specify things about the current project

### **Config project specification**

``` yaml
name_project: new_app
type_project: executable # executable | static_libarry | dynamic_libarary
description: Hello World in Next
version: v0.0.1
build_dir: build
```

### **Config Dependencies and Includes**

``` yaml
include_dirs:
- include
- template
# others local dirs
dependencies:
  nueva_lib:
    name: new_lib
    date: 22/7/2022
    dir: /home/user/docuemnts/new_lib
  other_libre:
    name: other_lib
    date: 20/7/2022
    dir: /home/user/desktop/other_lib
```

### **Config Builders**

``` yaml
builds:
  cmake_release:
    base: cmake
    build_system_exe: make
    c_compiler: gcc
    cxx_compiler: g++
    build_system: Unix Makefiles
    cmake_flags: []
    build_system_flags: [VERBOSE=1]
  cmake_debug:
    base: cmake
    build_system_exe: make
    c_compiler: clang
    cxx_compiler: clang++
    build_system: Unix Makefiles
    cmake_flags: []
    build_system_flags: [VERBOSE=1]
```

### **Config Export Library**

``` yaml
libarary: /home/user/documents/my_library/build/lib # .a .so .lib .dll
```

### **Config comand of exce**

```yaml
commands:
  src: cd src
  test: ./build/test.exe
```
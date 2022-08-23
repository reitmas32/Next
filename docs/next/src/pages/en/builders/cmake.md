---
title: Cmake Builder
description: How Create s Build based in Cmake
layout: ../../../layouts/MainLayout.astro
---

#### Dependencies

- [Cmake](https://cmake.org/)
- Builder Ninja, MSBuild or Unix Makefiles

#### Properties

| Property           | Description                 | Default        | Required | Type   | Example        |
| ------------------ | --------------------------- | -------------- | -------- | ------ | -------------- |
| base               | Buirder Base                | none           | Yes      | string | cmake          |
| name_out           | Name of Out **Development** | $build_name    | No       | string | my_app         |
| c_compiler         | Executable of C compiler    | gcc            | No       | string | clang          |
| cxx_compiler       | Executable of C++ compiler  | g++            | No       | string | clang++        |
| build_system_exe   | Executable of Build System  | make           | Yes      | string | make           |
| build_system       | Build System Name           | Unix Makefiles | Yes      | string | Unix Makefiles |
| cmake_flags        | Flags of Cmake              | none           | none     | list   | None           |
| build_system_flags | Falgs of Build System       | none           | none     | list   | None           |

#### Examples 

``` yaml
# Basic Setup for Builder
cmake_release:
    base: cmake
    build_system_exe: make
    c_compiler: gcc
    cxx_compiler: g++
    build_system: Unix Makefiles
    cmake_flags: []
    build_system_flags: []
```
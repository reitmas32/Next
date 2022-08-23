---
title: Basic Builder
description: How Create a Build based in Basic
layout: ../../../layouts/MainLayout.astro
---

#### Dependencies

- Only Compiler C or C++ and linker

#### Properties

| Property           | Description                | Default                  | Required | Type   | Example |
| ------------------ | -------------------------- | ------------------------ | -------- | ------ | ------- |
| base               | Buirder Base               | none                     | Yes      | string | basic   |
| name_out           | Name of Out                | $build_name              | No       | string | my_app  |
| c_compiler         | Executable of C compiler   | gcc                      | No       | string | clang   |
| cxx_compiler       | Executable of C++ compiler | g++                      | No       | string | clang++ |
| linker             | Executable of Linker       | g++                      | No       | string | ld      |
| source_cxx         | Source Files C++           | none                     | Yes      | list   | None    |
| source_c           | Source Files C             | none                     | Yes      | list   | None    |
| extension_files    | Extension of files         | none                     | No       | list   | None    |
| c_compiler_regex   | Simple Regex  C            | $C $FILE -o $FILE.o -c   | No       | string | None    |
| cxx_compiler_regex | Simple Regex  C++          | $CXX $FILE -o $FILE.o -c | No       | string | None    |
| linker_regex       | Simple Regex  Linker       | $LD $FILES -o $FILE_OUT  | No       | string | None    |

#### Examples

``` yaml
# Basic Setup for Builder
basic_minim:
    base: basic
    source_cxx:
      - src/*.cpp
    source_c:
      - src/*.c
```
``` yaml
# Full Setup for Builder
basic_release:
    base: basic
    name_out: my_app
    c_compiler: gcc
    cxx_compiler: clang++
    linker: ld
    source_cxx:
      - src/main.cpp
      - src/func/suma.cpp
      - src/suma.cpp
      - src/structs/*.cpp
    extension_files:
      - .cpp
      - .c
      - .cc
    c_compiler_regex:
      $C $FILE -o $FILE.o -c
    cxx_compiler_regex:
      $CXX -c $FILE -o $FILE_OUT
    linker_regex:
      $LD $FILES $FILE_OUT -std=c++20 -lGL -ptheard
```

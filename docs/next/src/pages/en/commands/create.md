---
title: Create Command
description: How Create a first Project
layout: ../../../layouts/MainLayout.astro
---

#### Description

Create a new Next project

#### Arguments and Options of Command


| Property     | Description          | Default    | Required | Type             | Example                                        |
| ------------ | -------------------- | ---------- | -------- | ---------------- | ---------------------------------------------- |
| name         | Name of Project      | none       | Yes      | string, argument | my_app                                         |
| build_dir    | Build Directory      | build      | No       | string, option   | bin                                            |
| name_build   | Name of Build        | app        | No       | string, option   | game                                           |
| type_project | Type of this project | executable | No       | string, option   | •executable  •static_library  •dinamic_library |
| base         | Builder Base         | basic      | No       | string, option   | cmake                                          |

#### Examples


``` bash
# Basic use
next create new_app
```

``` bash
# Full use
next create new_app --build_dir=bin --name_build=my_app --type_project=executable --base=cmake
```
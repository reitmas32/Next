---
title: Import Command
description: How Import Library in current Project
layout: ../../../layouts/MainLayout.astro
---

#### Description

How Import Library in current Project

#### Arguments and Options of Command


| Property         | Description              | Default | Required | Type             | Example                     |
| ---------------- | ------------------------ | ------- | -------- | ---------------- | --------------------------- |
| name_dependencie | Name of Dependencie      | None    | Yes      | string, argument | My_lib                      |
| dir              | Directory of Dependencie | None    | Yes      | string, argument | /home/user/documents/my_lib |

#### Examples


``` bash
# How to use
next import My_lib --dir=/home/user/documents/my_lib
```
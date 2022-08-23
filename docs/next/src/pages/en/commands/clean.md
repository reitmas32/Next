---
title: Clean Command
description: Clean the $build_dir
layout: ../../../layouts/MainLayout.astro
---

#### Description

Clean the $build_dir

#### Arguments and Options of Command


| Property | Description                              | Default    | Required | Type             | Example       |
| -------- | ---------------------------------------- | ---------- | -------- | ---------------- | ------------- |
| build    | Name of Builder to Clean **Development** | All Builds | No       | string, argument | cmake_release |

#### Examples


``` bash
# Basic use
next clean
```

``` bash
# Full use
next clean cmake_release
```
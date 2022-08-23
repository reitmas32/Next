---
title: Version Command
description: Get the version of Next
layout: ../../../layouts/MainLayout.astro
---

#### Description

Get the version of Next

#### Arguments and Options of Command


| Property | Description                                                     | Default | Required | Type        | Example |
| -------- | --------------------------------------------------------------- | ------- | -------- | ----------- | ------- |
| all      | Flag to get the version of all projects from $NEXT_PACKAGES_DIR | 0       | No       | int, option | 1       |

#### Examples


``` bash
# Basic use
next version
```

``` bash
# Full use
next version --all=1
```
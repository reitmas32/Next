---
title: Build Command
description: How Build the Project
layout: ../../../layouts/MainLayout.astro
---

#### Description

Build Next project

#### Arguments and Options of Command


| Property   | Description     | Default          | Required | Type             | Example       |
| ---------- | --------------- | ---------------- | -------- | ---------------- | ------------- |
| build_name | Name of Builder | First in $builds | No       | string, argument | cmake_release |

#### Examples


``` bash
# Basic use
next build
```

``` bash
# Full use
next build cmake_release
```

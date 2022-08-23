---
title: Get Command
description: How Get property of config.yaml
layout: ../../../layouts/MainLayout.astro
---

#### Description

How Get property of config.yaml

#### Arguments and Options of Command


| Property | Description                | Default | Required | Type             | Example      |
| -------- | -------------------------- | ------- | -------- | ---------------- | ------------ |
| property | Property to Get            | none    | Yes      | string, argument | name_project |
| comments | Get property with Comments | True    | No       | bool, option     | False        |

#### Examples


``` bash
# Basic use
next get name_project
```

``` bash
# Full use
next get name_project --comments=False
```
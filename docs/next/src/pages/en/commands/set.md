---
title: Set Command
description: Set property of config.yaml
layout: ../../../layouts/MainLayout.astro
---

#### Description

Set property of config.yaml

#### Arguments and Options of Command


| Property | Description           | Default | Required | Type             | Example  |
| -------- | --------------------- | ------- | -------- | ---------------- | -------- |
| property | Property to Set       | none    | Yes      | string, argument | name     |
| value    | New Value of Property | name    | Yes      | string, option   | this_app |

#### Examples


``` bash
# Basic use
next set name --value=this_app
```
---
title: Add Command
description: Add property to config.yaml
layout: ../../../layouts/MainLayout.astro
---

#### Description

Add property to config.yaml

#### Arguments and Options of Command


| Property | Description       | Default | Required | Type             | Example  |
| -------- | ----------------- | ------- | -------- | ---------------- | -------- |
| property | Property to Add   | none    | Yes      | string, argument | name     |
| value    | Value of Property | name    | Yes*     | string, option   | this_app |

#### Examples


``` bash
# How to use
next add name --value=this_app
```
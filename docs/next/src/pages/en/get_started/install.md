---
title: Install and Setup
description: How Install Next and Setup
layout: ../../../layouts/MainLayout.astro
---

### **Next is created with Python**

**Install with PyPi**

``` bash
pip install next-pm
```
    
**Install code stable**
``` bash
git clone https://github.com/reitmas32/Next.git
```

**Install code development**
``` bash
git clone https://github.com/reitmas32/Next.git
git checkout dev
```

**Setup**
``` bash
cd $HOME # if your System is Windows use %%LOCALAPPDATA%%
mkdir .next
cd .next/
echo 'NEXT_DIR:<DIR_OF_NEXT_INSTALATION>
NEXT_PACKAGES_DIR:<DIR_OF_NEXT_PACKAGES> > env.yaml
```
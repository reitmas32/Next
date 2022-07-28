---
title: Empty Project
description: How Create a Project from scratch
layout: ../../../layouts/MainLayout.astro
---

This section will talk about how to create a empty project with Next and how buiild the app

##### **Create the project**

```bash
mkdir empty_project # Create dir
cd empty_project/ # Get in
mkdir src # Create src dir
mkdir build # Create build dir
touch src/main.cpp # Create main file
```

##### **Write Code in main.cpp**

```c
//  src/main.cpp

#include <iostream>

int main(int argc, char const *argv[])
{
    std::cout << "Hello World with Next" << std::endl;
    return 0;
}
```

##### **Config the config.yaml file**

```
touch config.yaml
```

*Basics*

```yaml
# config.yaml
name_project: empty_project
type_project: executable
description: Empty project in Next
version: v0.0.1
build_dir: build
```

*Commands*

```yaml
# config.yaml
commands:
  build: g++ src/main.cpp -o build/app
  clean: rm -r build/app
  run: ./build/app
```
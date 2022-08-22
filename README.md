## **Next**
```
Manage your Next app development.

Common commands:

  next create <output directory>
    Create a new next project in the specified directory.

  next run [options]
    Run your Next application.

Usage: next <command> [arguments]

Global options:
-h, --help                  Print this usage information.

Available commands:
  add        Add to property of current Next Project
  build      Build a project of Next
  check_env  check env the NextPackages
  clean      Clean a project of Next
  create     Create a new project of Next
  exce       Add to property of current Next Project
  get        Get property of current Next Project
  info       view info the Next
  run        Run a project of Next
  set        Set property of current Next Project
  use        Add new library in current project
  version    view version the Nex

Run "next <command> --help" for more information about a command.

```
### **Install with PyPi**

``` bash
pip install next-pm
```
    
### **Install code stable**
``` bash
git clone https://github.com/reitmas32/Next.git
```

### **Install code development**
``` bash
git clone https://github.com/reitmas32/Next.git
git checkout dev
```

### Setup
``` bash
cd $HOME # if your System is Windows use $LOCALAPPDATA
mkdir .next
cd .next/
echo 'NEXT_DIR:<DIR_OF_NEXT_INSTALATION>
NEXT_PACKAGES_DIR:<DIR_OF_NEXT_PACKAGES> > env.yaml
```

### Contributors

**Next** is mainly supported by the development team of **Game Engine MOON** create by **EGE Studios** and currently managed by **Next.Project**

### Future versions

The current version of Next is **v3.4.0** but the development of Next is in constant evolution and it is planned to have for the next versions:
#### Commands
- **next upgrade** Easy update of **Next**
- **next test** Integration of **Next** and Unit Testing
- **next doctor** An easy way to view the status of C/C++ compilers
- **next pbuild** build custom programmer in python
- **next prun** run custom programmer in python
- **next ptest** test custom programmer in python
- **next pclean** clean custom programmer in python
- **next install** install package from [next.packages.com](https://www.next-packages.com)
- **next uninstall** uninstall package from [next.packages.com](https://www.next-packages.com)


#### Backend
- Dependency tree 
- Separate cmake logic from next to implement more construction systems
- MacOS support

#### Frotend
- Create a GUI
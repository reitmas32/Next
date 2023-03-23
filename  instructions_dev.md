# Next for Development

### **Create NEXT_PACKAGES_DIR and NEXT_DIR**
```bash
cd $HOME
mkdir Next_Packages
export NEXT_PACKAGES_DIR=$HOME/Next_Packages
export NEXT_DIR=$HOME/git/Next
```

### **Create Env**
```bash
mkdir venv
python3 -m venv/{DIR}
```

### **Activate Env**
```bash
#Linux and MacOS
source venv/{DIR}/bin/activate

#Windows
venv/{DIR}/bin/activate.bat
```

### **Install requirements.txt**
```bash
pip3 install -r requirements.txt
```
# ECC-CSPRNG
## Installation
```bash
git clone https://github.com/NL70/ecc-csprng.git 
```
## Setting up your environment
Note: Ensure you have [pip](https://pip.pypa.io/en/stable/installation/) and [Python 3](https://www.python.org/downloads/).
```bash
cd ecc-csprng
pip install virtualenv

# Creates a virtual environment 
python3 -m venv env

# Enters the virtual environment
source env/bin/activate # Linux
env/Scripts/activate.bat # Windows CMD
env/Scripts/Activate.ps1 # Windows Powershel


# Downloads dependencies
pip install -r requirements.txt

# Runs the program
python3 index.py
```

## Exiting venv
```bash
deactivate
```


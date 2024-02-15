# ECC-CSPRNG
## Installation
```bash
git clone https://github.com/NL70/ecc-csprng.git 
```
## Setting up your environment
Note: Ensure you have [pip installed](https://pip.pypa.io/en/stable/installation/).
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
```
## Executing the program
```bash
python3 index.py
```
## Exiting venv
```bash
deactivate
```


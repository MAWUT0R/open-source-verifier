# open-source-verifier
Algorand Opensource (AOS) Verifier is a tool that verifies the claimed source code of an Algorand on-chain application. It can be accessed temporarily at [https://aosverifier.appspot.com/](https://aosverifier.appspot.com/). To use the verification tool, you must provide the following:
1. An Algorand application ID
2. A public github url to an Algorand smart contract (Teal or Reach) file

## run locally
AOS Verifier is built using the [flask framework](https://flask.palletsprojects.com/en/2.2.x/), and can be run locally once cloned.

### pre-requisites
- Python3
- [pip](https://pypi.org/project/pip/)

### run flask app
```bash
git clone https://github.com/MAWUT0R/open-source-verifier.git
cd open-source-verifier
pip install -r requirements.txt
python3 main.py
```

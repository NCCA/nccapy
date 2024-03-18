# nccapy

The code in this python package is used in various units taught in the NCCA and in particlar [Jon's programming courses](https://nccastaff.bournemouth.ac.uk/jmacey/)

The aim of this repository is to teach not only about python [modules and packages](https://docs.python.org/3/tutorial/modules.html) but demonstrate other python code and techniques.

## Installation

This module is on [PyPi](https://pypi.org/project/nccapy/) so you can install it using pip

```bash
pip install nccapy
```



## Modules


## Developer notes

To build the package run the following command

```bash
python -m pip install build
python -m build
```

To run the tests use the following command

```
pytest -v .
```

for coverage reports use the following command

```bash
coverage run --source=src/nccapy -m pytest -v tests && coverage report -m
```

This will create a dist folder with the package in it. You can then install the package using pip

```bash
pip install dist/nccapy-0.0.1-py3-none-any.whl
```

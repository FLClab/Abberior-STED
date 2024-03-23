# Abberior-STED

This package interfaces the ``specpy`` package provided by Abberior GmbH using simple functions to configure the microscope. 

*This package is not maintained by Abberior.*

## Installation 

Install the ``specpy`` package provided with the Imspector software for your specific python version.

### PyPI

Installation from PyPI is done with
```bash
pip install abberior-sted
```

### Local install

The repository can be cloned locally and installed in editable mode
```bash
git clone https://https://github.com/FLClab/Abberior-STED
pip install -e Abberior-STED
```

## Usage

One the repository is installed, the user may simply import ``abberior`` as such
```python 
from abberior import microscope, user, utils
```

## Debug 

There is a debug mode that was implemented for testing purposes when ``specpy`` is not installed on the current computer. This is interesting in cases where you want to test a new part of the code while not being on a real microscope. To use the debug mode, the user may simply import the ``abberior`` module as you would normally do

```python 
>>> from abberior import microscope, user, utils
No module named 'specpy'
Calling these functions might raise an error.

Falling back to the debug files...
```

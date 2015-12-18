#!/usr/bin/env bash
#
# Note: venv activation etc requires bash!
#
# TODO: Move all this to python!

# Setup local venv (python3):

pyvenv venv
./venv/bin/pip install -U pip setuptools twine
./venv/bin/python setup.py install
./venv/bin/b2


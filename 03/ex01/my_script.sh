#!/bin/sh

pip --version
pip3 install -t local_lib git+https://github.com/jaraco/path.git --force-reinstall --upgrade > script.log
python3 my_program.py


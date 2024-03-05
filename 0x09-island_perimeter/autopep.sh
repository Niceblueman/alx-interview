#!/usr/bin/env bash
# Fixing code styling with pycodestyle for python 3.4
VENV='./env/*'

if [ ! "$(command -v pycodestyle)" ]
then
    echo "Missing package, start installing pycodestyle..."
    curl https://bootstrap.pypa.io/pip/3.4/get-pip.py -o .get-pip.py && python3 .get-pip.py
    sudo python3 -m pip install pycodestyle > /dev/null 2>&1
fi

echo -e "\n\nRunning pycodestyle..."
find . -type f -name '*.py' ! -path '*/migrations/*' ! -path "$VENV" -exec pycodestyle --verbose '{}' \; &&\

echo -e "\nDone"
#exit
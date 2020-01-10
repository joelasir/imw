#!/bin/bash

cd "$(dirname "$0")"
PYTHON_VENV=$(pipenv --venv)
uwsgi --socket :5000 --home $PYTHON_VENV -w main:app


#!/usr/bin/env bash

set -ex

cp -v $RECIPE_DIR/python/setup.py src/python

$PYTHON -m pip install -v src/python --no-deps

#!/usr/bin/env bash

pip-compile --resolver=backtracking --index-url=https://pypi.org/simple -o requirements/deployment.txt requirements/deployment.in
pip-compile --resolver=backtracking --index-url=https://pypi.org/simple -o requirements/development.txt requirements/development.in

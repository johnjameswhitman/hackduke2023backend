#!/usr/bin/env bash

pip-compile --resolver=backtracking -o requirements/deployment.txt requirements/deployment.in
pip-compile --resolver=backtracking -o requirements/development.txt requirements/development.in

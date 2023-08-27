#!/usr/bin/env bash

pip-compile --resolver=backtracking -o requirements.txt requirements.in

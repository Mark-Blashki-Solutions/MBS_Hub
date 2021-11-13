# MBS_Hub

Dashboard

## To run tests

> python -m coverage run -m pytest

## To generate coverage report

> python -m coverage html

## To run tests and get coverage for vscode

> python -m coverage run -m pytest; python -m coverage xml; python -m coverage report -m

### To skip slow tests

> python -m coverage run -m pytest -m "not slow"; python -m coverage xml; python -m coverage report -m

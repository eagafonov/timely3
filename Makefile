PYTHONPATH=$(shell pwd)
export PYTHONPATH


all:

check: flake pytest

flake:
	flake8 tests timely3

pytest:
	pytest tests

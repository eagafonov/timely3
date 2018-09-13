PYTHONPATH=$(shell pwd)
export PYTHONPATH


all:

check: flake pytest

flake:
	python3 -m flake8 tests timely3

pytest:
	python3 -m pytest tests

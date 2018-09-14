PYTHONPATH=$(shell pwd)
export PYTHONPATH


all:

check: flake pytest run-simple

flake:
	python3 -m flake8 tests timely3

pytest:
	python3 -m pytest --log-format="%(asctime)s %(levelname)s %(message)s" -v -s tests

run-simple:
	python3 examples/simple.py

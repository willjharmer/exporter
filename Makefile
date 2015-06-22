.PHONY: init clean server dev test spec features
.DEFAULT_GOAL := test

init:
	conda env create && source activate exporter

clean:
	find . -name '*.pyc' -delete

server:
	python manage.py runserver --host 0.0.0.0

dev:
	python manage.py runserver

test:
	python test_runner.py test

.PHONY: init create-env clean clean-wd clean-env server dev test spec features
.DEFAULT_GOAL := test

init: clean create-env

create-env:
	conda env create -n pydev -q QUIET;

clean: clean-env clean-wd

clean-wd:
	find . -name '*.pyc' -delete;

clean-env:
	conda env remove -n pydev -y;

server:
	python manage.py runserver --host 0.0.0.0;

dev:
	python manage.py runserver --port 6363;

test:
	python test_runner.py test;

test-watch:
	python WatchdogFile.py;

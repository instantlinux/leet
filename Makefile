PYPI_URL ?= https://nexus.instantlinux.net/repository/pypi/
PYPI_USER ?= svc_docker
RRSYNC_URL = https://www.samba.org/ftp/unpacked/rsync/support/rrsync
SSL_CHAIN ?= /usr/local/share/ca-certificates/instantlinux-ca.crt
VERSION ?= $(shell grep -o '[0-9.]*' code/_version.py)

VENV=python_env
VDIR=$(PWD)/$(VENV)

analysis: flake8
test: pytest
package: bin/rrsync dist/code-$(VERSION).tar.gz
publish: package
	@echo Publishing python package
	(. $(VDIR)/bin/activate && \
	 twine upload --cert=$(SSL_CHAIN) --repository-url $(PYPI_URL) \
	   -u $(PYPI_USER) -p $(PYPI_PASSWORD) dist/*)

test_functional:
	@echo "Run Functional Tests - not yet implemented"

flake8: test_requirements
	@echo "Running flake8 code analysis"
	(. $(VDIR)/bin/activate ; flake8 --exclude=python_env \
	 code tests)

python_env: $(VDIR)/bin/python

test_requirements: python_env
	@echo "Installing test requirements"
	(. $(VDIR)/bin/activate && \
	 pip install -r tests/requirements.txt)

$(VDIR)/bin/python:
	@echo "Creating virtual environment"
	virtualenv --system-site-packages $(VENV)

pytest: test_requirements
	@echo "Running pytest unit tests"
	cd code && \
	export PYTHONPATH=. && \
	(. $(VDIR)/bin/activate ; \
	py.test $(XARGS) ../tests/ \
	 --junitxml=../tests/results.xml \
	 --cov-report html \
	 --cov-report xml \
	 --cov-report term-missing \
	 --cov .)

dist/code-$(VERSION).tar.gz:
	@echo "Building package"
	pip show wheel >/dev/null; \
	if [ $$? -ne 0 ]; then \
	  (. $(VDIR)/bin/activate ; python setup.py sdist bdist_wheel); \
	else \
	  python setup.py sdist bdist_wheel ; \
	fi

bin/rrsync:
	@echo "Downloading rrsync"
	wget -q -O $@ $(RRSYNC_URL)
	chmod +x $@

clean:
	rm -rf build dist bin/rrsync code/htmlcov *.egg-info \
	 tests/__pycache__
	find . -regextype egrep -regex '.*(coverage.xml|results.xml|\.pyc|~)' \
	 -exec rm -rf {} \;
wipe_clean: clean
	rm -rf python_env

REQUIREMENTS_FILE=requirements.txt
PYTHON3-exists := $(shell command -v python3 2> /dev/null)
PIP-exists := $(shell command -v pip3 2> /dev/null)

check_python3:
ifndef PYTHON3-exists
	$(error "python3 is not available - please install it.")
endif

check_pip3:
ifndef PIP-exists
	$(error "pip3 is not available - please install it.")
endif

virtualenv: check_python3 check_pip3
	@echo Check if the software 'virtualenv' is installed.
	@echo [WARNING] Using 'pip' to install it in the user directory.
	hash virtualenv 2>/dev/null || pip3 install virtualenv

venv3: virtualenv venv/bin/activate
venv/bin/activate: requirements.txt
    ##############################
	#Install required dependencies
	#############################
	test -d venv || virtualenv --python=python3 venv
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

clean:
	##############################
	#Clean up any build files.###
	#############################
	python setup.py clean --all
	rm -rf build-*
	rm -rf *egg*
	rm -rf dist
	rm -rf docs/log_files/*.log

install_deps: venv3

remove_deps:
	-rm -rf venv

package:
    ##############################
	#Build wheel files        ###
	#############################
	python3 setup.py bdist_wheel
	##############################
	#Build success!!          ###
	#############################

test:
	##############################
	#Run all testes           ###
	#############################
	nosetests -v -s

install: clean install_deps test package

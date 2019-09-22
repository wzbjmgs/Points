REQUIREMENTS_FILE=requirements.txt
REQUIREMENTS_OUT=requirements.txt.log
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
	hash virtualenv 2>/dev/null || pip install virtualenv

venv3: virtualenv venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv --python=python3 venv
	venv/bin/pip install -r requirements.txt;
	touch venv/bin/activate

clean:
	# Clean up any build files.
	python setup.py clean --all
	#
	# Clean up everything else
	rm MANIFEST || true
	rm -rf build-*
	#
	# Clean up the egg files
	rm -rf *egg*
	#
	# Remove dist
	rm -rf dist
	#rm $(REQUIREMENTS_OUT)

install_deps: venv3

remove_deps:
	-rm -rf venv

package:
	# Generate the tarball based on MANIFEST.in
	python setup.py sdist
	#
	#
	# Build the python Egg
	python setup.py bdist_wheel
	#
	@echo
	@echo "Files to upload:"
	@echo "--------------------------"
	@ls -l ./dist/

check:
	# Run all the tests.
	nosetests -v -s

install: clean install_deps check package

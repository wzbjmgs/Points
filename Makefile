REQUIREMENTS_FILE=requirements.txt


venv3: requirements.txt
    ##############################
	#Install required dependencies
	#############################
	test -d venv || virtualenv --python=python3 venv
	venv/bin/pip install -r requirements.txt;
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
	python setup.py bdist_wheel
	##############################
	#Build success!!          ###
	#############################

test:
	##############################
	#Run all testes           ###
	#############################
	nosetests -v -s

install: clean install_deps test package

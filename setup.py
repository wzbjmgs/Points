import os

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

current_dir = os.path.dirname(os.path.realpath(__file__))
requirement_path = current_dir + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(name='points',
      version='1.0',
      long_description=readme,
      url='',
      license=license,
      author='Jayden',
      author_email='',
      install_requires=install_requires,
      description='Points MARS ROVERS Assignment',
      package_data={'': ['*.yml']},
      include_package_data=True,
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests', 'docs.*']))

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='points',
      version='1.0',
      long_description=readme,
      url='',
      license=license,
      author='Jayden',
      author_email='',
      description='Points MARS ROVERS Assignment',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests', 'docs.*']))

Points MARS ROVERS Problems
===========================

This is a assignment for points MARS ROVERS Problems.

## Installation

run following command to build project

```
make build
```

run following command to clean project

```
make clean
```

Decision:
1. Need requirement.txt specific the lib version. So that no matter
where to run this application, they always use same version
of dependenceis.

2. Build this application as egg file which can be pushed to pypi or
company local repo by using Jenkins pipeline, so that any other users can easily download and use it.

3. Use Makefile script to easy clean, build and run test of this project before release. Also, it could
be possible to build docker image and push to repo.

4. Logic to package python applicaiton. 
    1. Clean project.
    2. check whether python 3 and pip 3 are exist.
    3. Install dependencies into virtual environment.
    4. Run all tests.
    5. Build and package project.
    

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
    
5. Decide to use queue data structure to store rover data, because the requirement is second rover can't move
before first rover move. Queue has first in first out feature, so that I choose queue to store rover object.
Queue store rover command data, each command data is a queue also to make sure execute command in right order.
First: pop top rover command queue, then pop command need to be executed, after successfully execute the command,
push the rover command queue back to queue. At this time, the new pushed rover command queue at the bottom of the
queue which make sure that rover move one by one.
Since rover need to move one by one, so there is no need to use multi-thread approach.

6. When move conflict happened, e.g. rover 1 move to (1,2) already and second rover next move is (1,2) also,
second rover will pause a round and then move forward. Doing this because I want rover to execute all commands
to provide a complete view. If I abandon one command, and move to next command, it will change the rovers moving
plan and may not provide complete view.
Problem: deadlock, all rovers wait for each other.
# POINTS MARS ROVERS
===========================

This is a assignment for points MARS ROVERS problem.

## Input Data Model

- First input param is plateau coordiante, which is a string including two positive integers.
### Example
```
 "5 5"
```
- Second input param are rover information, which is a list including start position and move commands for each one rover.
### Example
```
  "[
 		['1 2 N', 'LMLMLMLMM'],
		['3 3 E', 'MMRMMRMRRM']
	]"
```

## Output Data Model

Each rover has a corresponding output string representing its coordinate and direction.

### Example
Here are two rovers' output separated by comma
```
['1 3 N', '5 1 E']
```

## How to clean project

Run following command in the root of project to clean

```
make clean
```

## How to Build

Makefile includes several targets such as cleanning project, installing dependences, running all unit tests and pakcaging application. It could also release wheel file to local or global repo (not implemented now). Run following command at the root of project will trigger all targets above.

```
make install
```

## How to Test

Run following command in the root of project to trigger all unit tests.
```
make test
```

## How to run application
### Approach 1:
Open your termianl, go to the root of project and run following command.

```
bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"
```
### Approach 2:
Clone this project to your local, and open it using e.g. pycharm. Find the app,py under Points/points/ directory, then run it directly. If no outside input data, it will use default input data.

### Approach 3:
Run application inside docker container.

- Run following command at the root of project to build points docker image.
```
docker build . -t points:latest
```

- Run following command at the root of to start a docker container.
```
docker run -i -t -d  points
```

- Run following command to run Points application inside the docker container.
```
docker exec <container-id> /bin/sh -c bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"
```

## How to check output

When you run the application, simple output data should display on the screen as following:
```
['1 3 N', '5 1 E']
```
While you can check the output in more details. For example: what is the move history for each rover, and whehter there is any exception situations happened. 

Move to Points/docs/log_files directory. There suppose to have two log files here.
1. info.log records all rovers' moving history.
2. errors.log recods all expcetion situation. For example, if the next move step is occupied by other rover already, I will stop the current rover and report the collision error to errors.log.






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

Test Data
"5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"

Run: 
1. run run.sh bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"
2. run docker run -i -t  points
3. After build docker image：docker build . -t points:latest
, and start docker container：  docker run -i -t -d  points
docker exec 32f45891c100 /bin/sh -c bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"
docker logs df090c008bb1 then you can see output

docker-compose up -d --force-recreate --build: re build and start points-app container


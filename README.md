# POINTS MARS ROVERS
===========================

This is a assignment for points MARS ROVERS problem.

## Input Data Model

- First input param is plateau coordiante, which is a string including two positive integers.
### Example
```
 "5 5"
```
- Second input param are rover information, which is a list including start position and move commands for each rover.
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

Run following command at the root of project to clean

```
make clean
```

## How to Build

Makefile includes several targets such as cleanning project, installing dependences, running all unit tests and pakcaging application. It could also release wheel file to local or global repo (not implemented now). Run following command at the root of project will trigger all targets above.

```
make install
```

## How to Test

Run following command at the root of project to trigger all unit tests.
```
make test
```

## How to run application
### Approach 1:
Open your termianl, go to the root of project and run following command.

```
bash run.sh "5 5" "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]"
```
"5 5" is plateau coordinate. "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'MMRMMRMRRM']]" is rover input data
### Approach 2:
Clone this project to your local, and open it using e.g. pycharm. Find the app.py under Points/points/ directory, then run it directly. If no outside input data, it will use default input data.

### Approach 3:
Install points.whl file and call app.py module

## How to check output

When you run the application, simple output should be displayed on the screen as following:
```
['1 3 N', '5 1 E']
```
These are final position data for two rovers.

While you can check the output in more details. For example: what is the move history for each rover, and any exception situations happened. 

Move to Points/docs/log_files directory. There suppose to have two log files.
1. info.log records all rovers' moving history.
2. errors.log records all exception situations. For example, if the next move coordinate is occupied by other rover already, I will stop the current rover and log the collision error to errors.log.
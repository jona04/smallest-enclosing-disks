# Smallest Enclosing Disks
## _Welzl Algorithm and Hearn Algorithm_

Two algoritmos to solve the problem Smallest Enclosing Disks (SED):
- Welzl Algorithm - based on "D. Jack Elzinga, Donald W. Hearn, (1972) The Minimum Covering Sphere Problem. Management Science 19(1):96-104".
- Hearn Algorithm - based in "Smallest enclosing disks (balls and ellipsoids)", in Maurer, H. (ed.), New Results and New Trends in Computer Science, Lecture Notes in Computer Science, vol. 555, Springer-Verlag, pp. 359–370"

## Install
```sh
pip install requirements.txt
```


## Generate data points
```sh
python3 ./genarate_points.py <quantity of points>
```

## Usage
```sh
python3 ./main.py <file-with-points>
```


In the main file there are all the code necessary to read the data file and to call both algorithms: Welzl Algorithm (recursive approach) and Hearn Algorithm (Quadratic programin approach).

In the Welzl Algorithm call was defined a limit of 500 data points:
Reason to it is the limite of recursive operations, this value can vary to computer.

The Hearn Algorithm there is not limite of data points.
Some results related to performance can be seen in the 'Smallest-Enclosed-Disks.pdf'. 


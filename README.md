# smallest-enclosing-disks
Two algoritmos to solve the problem Smallest Enclosing Disks (SED) - Welzl Algorithm and Quadratic Programming based algorithm

Install requirements.txt
pip install requirements.txt

Generate data points
python3 ./genarate_points.py <quantity of points>

Usage
python3 ./main.py <file-with-points>

In the main file there are all the code necessary to read the data file and to call both algorithms: Welzl Algorithm (recursive approach) and Hearn Algorithm (Quadratic programin approach).

In the Welzl Algorithm call was defined a limit of 500 data points:
Reason to it is the limite of recursive operations, this value can vary to computer.

The Hearn Algorithm there is not limite of data points.
Some results related to performance can be seen in the 'Smallest-Enclosed-Disks.pdf'. 


from sys import argv
import numpy as np
import csv

if len(argv) < 2:
    print('Usage: python3 ./generate_points.py <quantity of points>')
    exit(1)

# quanti of points
n = int(argv[1])

# generates two  list, axis x and axis y, with rondomly float values
# between -15 and 15  
axis_x = np.random.uniform(low=-15, high=15, size=(n,))
axis_y = np.random.uniform(low=-15, high=15, size=(n,))
points = [list(axis_x),list(axis_y)]

# export the two lists in a .txt file
with open('points.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for line in points:
        spamwriter.writerow(line)
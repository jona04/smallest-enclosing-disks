from sys import argv
import numpy as np

if len(argv) < 2:
    print('Usage: python3 ./generate_points.py <quantity of points>')
    exit(1)

# quanti of points
n = argv[1]

# generates two  list, axis x and axis y, with rondomly float values
# between -15 and 15  
axis_x = np.random.uniform(low=-15, high=15, size=(n,))
axis_y = np.random.uniform(low=-15, high=15, size=(n,))

# export the two lists in a .txt file
a_file = open("test.txt", "w")

np.savetxt(a_file, axis_x)
np.savetxt(a_file, axis_y)

a_file.close()
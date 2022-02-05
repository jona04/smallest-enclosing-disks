import csv
import matplotlib.pyplot as plt

from time import process_time
from util import *
from hearn_algorithm import *
from welzl_algorithm import *
from sys import argv


if len(argv) < 2:
    print('Usage: python3 ./main.py <file-with-points>')
    exit(1)

'''
Code block responsible to manipulate the data from the file
'''
data = []
with open('points.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    line = []
    for row in spamreader:
        line.append(row)
    data.append(line)
points = data[0]
points[0] = [float(x) for x in points[0]]
points[1] = [float(x) for x in points[1]]


'''
Code block responsible to execute Welzl algorithm
'''
if len(points[0]) < 500: # neccessary to avoid error in recursive limit operations
    xy = list(zip(points[0], points[1]))
    t1_start = process_time()
    result_welzl = minidisk(xy)
    t1_stop = process_time()
    print(" ")
    print("### Result Hear Algorithim: ####")
    print("center: ",result_welzl[0])
    print("radius: ",result_welzl[1])
    print("time: ",t1_stop) 
    print(" ")

    '''
    Code block responsable to generate results of Welzl Algorithm
    '''
    # fig, axes = plt.subplots()
    # earth = plt.Circle((result_welzl[0]),result_welzl[1], color = 'blue',fill=False )
    # plt.gca().set_aspect('equal', adjustable='box')
    # axes.add_patch(earth)
    # plt.scatter(points[0], points[1])
    # plt.title("Welzl Algorithm (Recursive Approach)")
    # plt.xlabel("Axis x")
    # plt.ylabel("Axis y")



'''
Code block responsible execute Hearn algorithm
'''
ax_global = points[0]
ay_global = points[1]
m = len(ax_global)
n = 2
there_is_negative_values_in_x = any(n < 0 for n in ax_global)
there_is_negative_values_in_y = any(n < 0 for n in ay_global)

adjust_x = 0
adjust_y = 0
if there_is_negative_values_in_x:
    ax_global,adjust_x = change_negative_values(ax_global,m)
if there_is_negative_values_in_y:
    ay_global,adjust_y = change_negative_values(ay_global,m)

points_list_global = []
for i in range(n+2,m):
    points_list_global.append((ax_global[i],ay_global[i]))

ax_points = []
ay_points = []
for i in range(0,n+2):
    ax_points.append(ax_global[i])
    ay_points.append(ay_global[i])

t2_start = process_time()
result,radius,it = algorithm(ax_points,ay_points,ax_global,ay_global,n,points_list_global)
t2_stop = process_time()
if there_is_negative_values_in_x:
    result[0]=result[0]+adjust_x
if there_is_negative_values_in_y:
    result[1]=result[1]+adjust_y
print(" ")
print("### Result Hear Algorithim: ####")
print("center: ",result)
print("radius: ",radius)
print("time: ",t2_stop) 
print("iterations: ",it)
print(" ")

'''
Code block responsable to generate results of Hearn Algorithm
'''
fig, axes = plt.subplots()
earth = plt.Circle((result),radius, color = 'blue',fill=False )
plt.gca().set_aspect('equal', adjustable='box')
axes.add_patch(earth)
plt.scatter(points[0], points[1])
plt.title("Hearn Algorithm (Quadratic Programing Approach)")
plt.xlabel("Axis x")
plt.ylabel("Axis y")


plt.show()
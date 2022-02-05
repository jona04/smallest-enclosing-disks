from random import *
from math import sqrt
import numpy as np


def all_points_in_sphere(x,radius,ax_global,ay_global,points_list_global):
    flag = True
#     check if all points is inside
    tuple_a = zip(ax_global, ay_global)
    for a in tuple_a:
        if is_inside(x,radius, a) == False:
            flag = False
        else:
            if a in points_list_global:
                points_list_global.remove(a)

    return flag

    
# Helper method to get a circle defined by 3 points
def get_circle_center(bx, by,
                        cx, cy):
    B = bx * bx + by * by
    C = cx * cx + cy * cy
    D = bx * cy - by * cx
    return [(cy * B - by * C) / (2 * D),
             (bx * C - cx * B) / (2 * D)]

# Function to return the euclidean distance
# between two points
def dist(a, b):
    return sqrt(pow(a[0] - b[0], 2)
                + pow(a[1] - b[1], 2))



# Function to check whether a point lies inside
# or on the boundaries of the circle
def is_inside(center,radius, p):
    return dist(center, p) <= radius


# To find the equation of the circle when
# three points are given.
 

def get_radius(ax_,ay_,v,basis,n):
    
    # Function to return a unique circle that
    # intersects three points
    p = []
    for i in range(n):
        if v[i] != 0 and i+2+n in basis.values():
            p.append((ax_[i],ay_[i]))
    
    if (len(p) == 1) :
        return [p[0], 0]
    
    if len(p) == 2:
        C = (p[0][0] + p[1][0]) / 2.0, (p[0][1] + p[1][1]) / 2.0 
        # Set the radius to be half the distance AB
        return C, dist(p[0], p[1]) / 2.0
    
    I = get_circle_center(p[1][0] - p[0][0], p[1][1] - p[0][1],
                            p[2][0] - p[0][0], p[2][1] - p[0][1])

    I[0] += p[0][0]
    I[1] += p[0][1]
    return I,dist(I, p[0])


# circle for N <= 3
def min_circle_trivial(P):
    if not P :
        return [(0,0),0]
     
    elif (len(P) == 1) :
        return [P[0], 0]
    
    # Function to return the smallest circle
    # that intersects 2 points
    elif (len(P) == 2) :
        # Set the center to be the midpoint of A and B
        C = (P[0][0] + P[1][0]) / 2.0, (P[0][1] + P[1][1]) / 2.0 
        # Set the radius to be half the distance AB
        return [C, dist(P[0], P[1]) / 2.0] 
         
    
    # Function to return a unique circle that
    # intersects three points
    I = get_circle_center(P[1][0] - P[0][0], P[1][1] - P[0][1],
                                P[2][0] - P[0][0], P[2][1] - P[0][1])
 
    I[0] += P[0][0]
    I[1] += P[0][1]
    return [I, dist(I, P[0])]
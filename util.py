from random import *
from math import sqrt
import numpy as np


def update_tableau_with_new_point(basis,ax_points,ay_points,next_point,n):
    v_in_basis = [ x - n-2-2 for x in basis.values() if x > 5 ]
    no_in_basis = np.setdiff1d([0,1,2,3],v_in_basis)

    if len(no_in_basis) == 1:
        ax_points.pop(v_in_basis[0])
        ay_points.pop(v_in_basis[0])
    else:
        ax_points.pop(no_in_basis[0])
        ay_points.pop(no_in_basis[0])

    ax_points.append(next_point[0])
    ay_points.append(next_point[1])

    return ax_points,ay_points

def check_negative_values(ax_global,ay_global,m):
    adjust_x = 0
    adjust_y = 0
    if any(n < 0 for n in ax_global):
        ax_global,adjust_x = change_negative_values(ax_global,m)
    if any(n < 0 for n in ay_global):
        ay_global,adjust_y = change_negative_values(ay_global,m)

    return adjust_x,adjust_y,ax_global,ay_global


def simplex(tab,n):
    
    stop = False
    iterator = 1
    basis = {}
    while stop == False:
        if iterator == 1:
            row = 0
            column = 2+n
        elif iterator == 2:
            row = 1
            column = 2+n-1
        else:
            row = np.argmin(tab[:,0], axis=0)
            column = get_column_simplex(tab,n,basis,row)
        
        basis[row] = column
        
        pivotDenom = tab[row][column]
        tab[row] = [x / pivotDenom for x in tab[row]]

        for k,line in enumerate(tab):
            if k != row:
                pivotRowMultiple = [y * tab[k][column] for y in tab[row]]
                tab[k] = [x - y for x,y in zip(tab[k], pivotRowMultiple)]
               
        if iterator > 2:
            if any(val < 0 for val in tab[:,0]) == False:
                stop = True

        # max iterations
        if iterator > 100:
            print("max iterations reached!")
            return tab,basis
        
        iterator = iterator + 1

    return tab,basis


def create_tableau(ax_,ay_,n):
    value_column = [[1]]
    for i in range(0,n):
        value_column.append( [(ax_[i]**2 + ay_[i]**2) * -1])
    value_column = np.asarray(value_column)

    i = np.identity(n)
    v_zeros = np.zeros(n)
    ui = np.concatenate(([v_zeros],i), axis=0)
    
    v_ones = np.ones((n,1))
    one_zero = np.zeros(1)
    w = np.concatenate(([one_zero],v_ones), axis=0)
    
    v_matrix = [np.ones(n)]
    for i in range(0,n):
        v_line = []
        for j in range(0,n):
            v_line.append(-2* (ax_[i]*ax_[j]+ay_[i]*ay_[j]))
        
        v_line = np.asarray(v_line)
        v_matrix = np.concatenate((v_matrix,[v_line]), axis=0)
    
    v_zeros_t = np.zeros((n,1))
    one_one = np.ones(1)
    y = np.concatenate(([one_one],v_zeros_t), axis=0)
    
    value_ui = np.c_[value_column,ui]
    w_vi = np.c_[w,v_matrix]
    w_vi_y = np.c_[w_vi,y]
    return np.c_[value_ui,w_vi_y]


def get_column_simplex(tab,n,basis,row):
    vi = tab[row,1:10]
    value_row = tab[row,0]
    div = -100
    new_column = 0
    for i,val in enumerate(vi):
        col = 1+i
        if col not in basis.values():
            div_aux = val/value_row
            if div_aux > 0 and div_aux > div:
                div = div_aux
                new_column = col
    return new_column


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

def get_point_outside_of_the_circle(x,radius,ax_global,ay_global):
    tuple_a = zip(ax_global, ay_global)
    outside = []
    for a in tuple_a:
        if is_inside(x,radius, a) == False:
            outside.append(a)
    distance = 0;
    idx = 0
    for i,val in enumerate(outside):
        aux_distance = dist(x,val)
        if aux_distance > distance:
            distance = aux_distance
            idx = i
    return outside.pop(idx)
         
def get_more_distant_point(x,points_list_global):
    distance = 0
    idx = 0
    for i,val in enumerate(points_list_global):
        aux_distance = dist(x,val)
        if aux_distance > distance:
            distance = aux_distance
            idx = i

    return points_list_global.pop(idx),points_list_global

# get the lagrangian variable v
def get_lagragian_variables(tab,basis,n):
    v = np.zeros(n)
    for i,val in enumerate(basis):
        if i == 0:
            v[i] = tab[:,0][val]
        elif i > 1:
            v[val-1] = tab[:,0][val]
    return v

def change_negative_values(a,m):
    min_a = min(a)-1
    new_a = []
    for i in range(0,m):
        new_a.append(a[i]+abs(min_a))
    
    return new_a,min_a


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
import numpy as np

from math import sqrt
from util import *


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

#         print("Next pivot index is=%d,%d \n" % (row,column))
        
        for k,row_no_used in enumerate(tab):
            if k != row:
                pivotRowMultiple = [y * tab[k][column] for y in tab[row]]
                tab[k] = [x - y for x,y in zip(tab[k], pivotRowMultiple)]
                
        
        if iterator > 2:
            if any(val < 0 for val in tab[:,0]) == False:
                stop = True

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

def algorithm(ax_points,ay_points,ax_global,ay_global,n,points_list_global):
    stop = False
    it = 1
    while  stop == False:
#         print("iteracoes",it)
        tab = create_tableau(ax_points,ay_points,n+2)
        # print(tab)
        tab,basis = simplex(tab,n+2)

        # get the lagrangian variable v
        v = get_lagragian_variables(tab,basis,n+2)

        # get center and radius
        x,radius = get_radius(ax_points,ay_points,v,basis,n+2)
        
        if all_points_in_sphere(x,radius,ax_global,ay_global,points_list_global):
            # print("optimal find",x)
            stop = True
        else:
            if len(points_list_global) > 0:
#                 get more distant point
                next_point,points_list_global = get_more_distant_point(x,points_list_global)
                # remove point from the tableau
                v_in_basis = [ x - n-2-2 for x in basis.values() if x > 5 ]
                no_in_basis = np.setdiff1d([0,1,2,3],v_in_basis)
                ax_points.pop(no_in_basis[0])
                ay_points.pop(no_in_basis[0])
                
                # add new point in the tableau
                ax_points.append(next_point[0])
                ay_points.append(next_point[1])
            else:
#                 get point outside of the circle
                next_point = get_point_outside_of_the_circle(x,radius,ax_global,ay_global)
    
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
        
        if it > 100:
            stop = True

        it = it + 1

    return [x[0],x[1]],radius,it
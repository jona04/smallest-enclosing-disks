from math import sqrt
from util import *


def algorithm(ax_points,ay_points,ax_global,ay_global,n,points_list_global):
    """ Iteractive method responsible to find the smallest enclosed disk using hearn algorithm
        
        Args:
            ax_points (list): first points to be optmized at the axis x
            ay_points (list): first points to be optmized at the axis y
            ax_global (list): quantity of points at the axis x
            ay_global (list): quantity of points at the axis y
            n (int): quantity of points
            points_list_global (list): list of  points (tuple) that need to be optimized
            
        Returns:
            return a tuple as the center of a circle, the radius of the circle and the number of iterations
    """
    stop = False
    it = 1
    while  stop == False:

        tab = create_tableau(ax_points,ay_points,n+2)
        
        # calculate optimization with 4 points using simplex
        tab,basis = simplex(tab,n+2)

        # get the lagrangian variable v
        v = get_lagragian_variables(tab,basis,n+2)

        # get center and radius based on the points from simplex
        x,radius = get_radius(ax_points,ay_points,v,basis,n+2)
        
        # check if all point is inside of the sphere generated in the last step
        if all_points_in_sphere(x,radius,ax_global,ay_global,points_list_global):
            stop = True
        # otherwise, remove one point of the soluion and insert another one no used yet
        else:
            # get point not used yet from a list
            if len(points_list_global) > 0:

                # get more distant point
                next_point,points_list_global = get_more_distant_point(x,points_list_global)
                
                # update tableau with new point
                ax_points,ay_points = update_tableau_with_new_point(basis,ax_points,ay_points,next_point,2)

            # if there is no avaible points in the list, and still there is point outside of the sphere,
            # we choose the most distant point outside the sphere and remove one point of the current solution to
            # to calculate the optimization again
            else:
                # get point outside of the circle
                next_point = get_point_outside_of_the_circle(x,radius,ax_global,ay_global)
    
                 # update tableau with new point
                ax_points,ay_points = update_tableau_with_new_point(basis,ax_points,ay_points,next_point,2)

        # max iterations
        if it > 100:
            stop = True

        it = it + 1

    return [x[0],x[1]],radius,it

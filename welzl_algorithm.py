from random import *
from util import *


def b_minidisk(P, R, n):
    """ Recursive method to get a circle compose by a center and a radius
        
        Args:
            P (list): Points to be allocated inside of the circle
            R (list): Points on the boudary of the circle
            n (int): quantity of points
            
        Returns:
            return a tuple as the center of a circle and the radius of the circle
    """
    
    # basic case
    if (n == 0 or len(R) == 3) :
        return min_circle_trivial(R)
 
    # get a random point
    idx = randint(0,n-1)
    p = P[idx]
 
    # Put the picked point at the end of P
    # since it's more efficient than
    # deleting from the middle of the vector
    P[idx], P[n - 1]=P[n-1],P[idx]
 
    # Get the MEC circle d from the
    # set of points P - :p
    d = b_minidisk(P, R.copy(), n - 1)
     
    center =  d[0]
    radius = d[1]
    # If d contains p, return d
    if (is_inside(center,radius, p)) :
        return d
     
 
    # Otherwise, must be on the boundary of the MEC
    R.append(p)
 
    # Return the MEC for P - :p and R U :p
    return b_minidisk(P, R.copy(), n - 1)


def minidisk(P):
    return b_minidisk(P, [], len(P))
from random import *
from util import *


def b_minidisk(P, R, n):
    """ Method  responsible for
        
        Args:
            P (): ss
            R (): asasd
            n (): asdasd
            
        Returns:
            return
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
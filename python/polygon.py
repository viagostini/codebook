def ccw(u, v, w):
    '''
    Returns a positive number if u -> v -> w is a counter-clockwise angle
            a negative number if u -> v -> w is a clockwise angle
            zero if u -> v -> w are colinear
    '''
    return (v[0] - u[0]) * (w[1] - u[1]) - (v[1] - u[1]) * (w[0] - u[0])

def is_convex(points):
    '''
    Returns True if polygon given by points is convex, False otherwise.

    Assumes that points is a list of points in counter-clockwise order.
    '''
    n = len(points)

    for i in range(n):
        u = points[i]
        v = points[(i + 1) % n]
        w = points[(i + 2) % n]
       
        if ccw(u, v, w) <= 0:
            return False

    return True

def area(points):
    '''
    Calculates area of simple polygon given by a list of points.

    Assumes that points is a list of points in either clockwise
    or counter-clockwise order.
    '''

    area, n = 0, len(points)
    
    for i in range(n):
        v, w = points[i], points[(i + 1) % n]
        area += v[0]*w[1] - v[1]*w[0]
    
    return abs(area) / 2
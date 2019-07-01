from numpy import *

def applyGivensRotation (rot,v):
    s = rot[0]
    c = rot[1]

    rotMatrix = array([
        [ c, s],
        [-s, c]
    ])

    return rotMatrix.dot(v)

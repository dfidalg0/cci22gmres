from numpy import *
from numpy.linalg import norm, LinAlgError

def applyGivensRotation (rot,v):
    s = rot[0]
    c = rot[1]

    rotMatrix = array([
        [ c, s],
        [-s, c]
    ])

    return rotMatrix.dot(v)

def getGivensRotation (v):
    m = norm(v)
    s = v[1]/m
    c = v[0]/m

    return (s,c)

def triangularSolve (A,b):
    n = b.size
    x = b.copy()
    for i in range(n-1,-1,-1):
        x[i] = (x[i] - A[i,i+1:n].dot(x[i+1:n]))/A[i,i]
    return x

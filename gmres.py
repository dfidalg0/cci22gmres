from utils import *

def GMRES (A,b,tolerance = 1e-6):
    _testForErrors(A,b)

    n = b.size

    v = b.copy()
    H = zeros([n+1,n])
    Q = zeros([n,n])

    rotations = [None]*n
    rotations[0] = (0,1) # Rotação de 0 rad

    for j in range(n):
        

def _testForErrors (A,b):
    err = (
        len(A.shape) != 2 or \
        A.shape[0] != A.shape[1] or \
        len(b.shape) != 1 or \
        A.shape[0] != b.shape[0]
    )

    if err:
        raise ValueError ('Invalid matrix shapes for solving linear system')

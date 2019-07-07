from gmres import *

A = array([
    [1,1,0,0],
    [1,2,1,0],
    [0,1,3,4],
    [0,0,1,5]
])

b = array([19,11,24,18])

x,err = GMRES(A,b,1e-3)

print(x)
print(err)

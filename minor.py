from gmres import *

A = array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
])

b = array([1,1,3,1])

x,err = GMRES(A,b)

print(x)
print(err)

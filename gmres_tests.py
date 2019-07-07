# Testes de funcionamento do GMRES
from solveMethods import GMRES
from numpy import *
from numpy.linalg import LinAlgError
from numpy.random import rand, randint
from timeit import default_timer

# Teste 1 - Sistema denso

n = 100

A = rand(n,n)*100

b = rand(n)*100

t0 = default_timer()
try:
    x,err = GMRES(A,b)
    t1 = default_timer()
except:
    print('Something went wrong')
else:
    print('Successfully executed')
    print('Time elapsed for dense system:',t1-t0)

# Teste 2 - Sistema esparso

for i in range(100*50):
    A[randint(100)][randint(100)] = 0

t0 = default_timer()
try:
    x,err = GMRES(A,b)
    t1 = default_timer()
except:
    print('Something went wrong')
else:
    print('Successfully executed')
    print('Time elapsed for sparse system:',t1-t0)

# Teste 3 - Sistema singular

A[1,:] = A[0,:]
try:
    GMRES(A,b)
except LinAlgError:
    print('Handling singular matrixes properly')
else:
    print('Singular matrixes not being properly handled')

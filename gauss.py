from utils import *

def GaussElimination (A,b):
    assertValidSystem(A,b) # Verificação de erros

    U = A.copy()
    v = b.copy()

    n = b.size

    for i in range(n-1):
        m = i + argmax(U[i:,i])
        if m != i:
            U[[i,m]],v[[i,m]] = U[[m,i]],v[[m,i]]

        for j in range(i+1,n):
            k = U[j,i]/U[i,i]
            U[j] -= k*U[i]
            v[j] -= k*v[i]

    return triangularSolve(U,v)

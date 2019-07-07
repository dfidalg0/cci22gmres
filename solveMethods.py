# Importando funções do numpy e de algebra linear
from utils import *
from numpy.linalg import solve

NumpySolve = solve
NumpySolve.__name__ = 'NumpySolve'

def GMRES (A,b,tolerance = 1e-6):
    assertValidSystem(A,b) # Verificação de erros

    n = b.size

    v = b.copy()
    H = zeros([n+1,n])
    Q = zeros([n,n])

    h = norm(v)

    u = array([h] + [0]*n) # u = ||b||*e1

    rotations = [None]*n # Vetor para armazenar as rotações de Given acumuladas

    ERR = [None]*n # Vetor para armazenar os erros das iterações

    err = 1

    for j in range(n):
        Q[:,j] = v/h
        v = A.dot(Q[:,j])

        H[0,j] = Q[:,0].dot(v)
        v -= H[0,j]*Q[:,0]

        for i in range(j):
            H[i+1,j] = Q[:,i+1].dot(v)
            v -= H[i+1,j]*Q[:,i+1]
            # Aplicação das rotações de Givens acumuladas
            H[i:i+2,j] = applyGivensRotation(rotations[i],H[i:i+2,j])

        h = norm(v)
        H[j+1,j] = h

        rot = rotations[j] = getGivensRotation(H[j:j+2,j])

        H[j:j+2,j] = applyGivensRotation(rot,H[j:j+2,j])
        u[j:j+2] = applyGivensRotation(rot,u[j:j+2])

        ERR[j] = err = abs(rotations[j][0]*err) # Erro calculado com base nas rotações de Givens acumuladas

        if err < tolerance:
            z = triangularSolve(H[:j+1,:j+1],u[:j+1])
            x = Q[:,:j+1].dot(z)
            ERR = array(ERR)
            ERR = ERR[ERR != None]
            return x,ERR

    raise LinAlgError ('Singular Matrix') # Matriz muito mal condicionada

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

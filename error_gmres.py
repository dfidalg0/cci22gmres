from matplotlib.pyplot import *
from numpy import *
from numpy.random import rand
from numpy.linalg import eig
from solveMethods import GMRES

N = 100

# Randomizando matriz A
A = rand(N,N)*100

# Tornando A simétrica para garantir que todos os seus autovalores são reais
for i in range(N):
    for j in range(i):
        A[i,j] = A[j,i]

l,v = eig(A)

errors = {}

for n in [12,25,50,100]:
    b = zeros(N)
    for j in range(n):
        b += (1 + rand()*99)*v[:,j]

    x,errors[n] = GMRES(A,b)

legends = errors.keys()
graphs = []

for key in legends:
    err = errors[key]
    ax, = plot(arange(1,len(err)+1),err)
    graphs.append(ax)

legend(graphs,legends)

xlabel('Número de iterações')
ylabel('Erro relativo')

show()

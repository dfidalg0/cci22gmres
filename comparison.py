from gauss import *
from gmres import *
from numpy.random import rand
from numpy.linalg import eig,solve
from matplotlib.pyplot import *
from timeit import default_timer

solve.__name__ = 'NumpySolve'

N = 100

A = rand(N,N)*100

for i in range(N):
    for j in range(i):
        A[i,j] = A[j,i]

l,v = eig(A)

methods = [GMRES,GaussElimination,solve]

T = {
    method.__name__ : [] for method in methods
}

for method in methods:
    print(method.__name__)
    for n in range(1,N+1):
        b = zeros(N)
        for j in range(n):
            b += rand()*100*v[:,j]

        t = [0]*50
        for i in range(20):
            t0 = default_timer()
            method(A,b)
            t1 = default_timer()

            t.append(t1-t0)

        T[method.__name__].append(mean(t))
        print('\rProgress: {:3d}%'.format((n*100)//N),end = '')
    print()

graphs = []

for method in T.keys():
    ax, = plot(arange(1,N+1),T[method])
    graphs.append(ax)

legends = [method.__name__ for method in methods]

legend(graphs,legends)

xlabel('Número de vetores na base')
ylabel('Tempo de execução')

show()

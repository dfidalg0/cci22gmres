from solveMethods import *
from numpy.random import rand
from numpy.linalg import eig
from matplotlib.pyplot import *
from timeit import default_timer

N = 100

# Randomizando matriz A
A = rand(N,N)*100

# Tornando A simétrica para garantir que todos os seus autovalores são reais
for i in range(N):
    for j in range(i):
        A[i,j] = A[j,i]

l,v = eig(A)

# Métodos de resolução a serem utilizados
methods = [GMRES,GaussElimination,NumpySolve]

# Tempos de execução de cada método
T = {
    method.__name__ : [] for method in methods
}

for method in methods:
    print(method.__name__)
    for n in range(1,N+1):
        b = zeros(N)
        for j in range(n):
            b += (1 + rand()*99)*v[:,j]

        t = [0]*35
        for i in range(35):
            t0 = default_timer()
            method(A,b)
            t1 = default_timer()

            t.append(t1-t0)

        T[method.__name__].append(mean(t))
        print('\rProgress: {:3d}%'.format((n*100)//N),end = '')
    print()

# Plot do gráfico
graphs = []

legends = T.keys()

for method in legends:
    ax, = plot(arange(1,N+1),T[method])
    graphs.append(ax)

legend(graphs,legends)

xlabel('Número de vetores na base')
ylabel('Tempo de execução')

show()

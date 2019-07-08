# Resolução de sistemas lineares

## Dependências
<table>
    <tr>
        <td> Python
    </tr>
    <tr>
        <td> numpy
    </tr>
    <tr>
        <td> matplotlib
    </tr>
</table>

## Algoritmos
O arquivo *solveMethods.py* contém os seguintes métodos de resolução de sistemas lineares

- *GMRES* - Resolução pelo método de resíduos mínimos generalizados
- *GaussElimination* - Resolução pelo método da eliminação de Gauss
- *NumpySolve* - Resolução implementada no módulo *numpy*

## Instruções de uso
Para utilizar um dos métodos contidos no módulo *solveMethods*, basta utilizar o comando

~~~python
from solveMethods import <method>
~~~

O script *comparison.py* compara os três métodos presentes na resolução de um sistema simétrico 100x100 aleatório **Ax = b** e plota um gráfico do tempo de execução de cada método em função do número de vetores da base de autovetores necessários para expressar o vetor **b**.

O script *gmres_tests.py* verifica se o algoritmo *GMRES* está se comportando corretamente.

## Funções

~~~python
GMRES (A,b, tolerance=1e-6)
~~~

> Argumentos:
> - A: Array quadrado do numpy
> - b: Array linear do numpy
>
> Retorno:
> - x : Solução do sistema Ax = b
> - ERR : Vetor com os erros de cada iteração

~~~python
GaussElimination(A,b)
~~~

> Argumentos:
> - A: Array quadrado do numpy
> - b: Array linear do numpy
>
> Retorno:
> - x : Solução do sistema Ax = b

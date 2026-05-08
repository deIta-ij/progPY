# Faz uma função recursiva que ordena o vetor usando a seguinte ideia:
#    Acha o menor valor do vetor.
#    Troca o primeiro elemento do vetor com o valor que encontrou, 
#    ou seja, o primeiro valor (o menor) agora está no lugar certo.
#    Faz o mesmo de forma recursiva para o vetor que começa na segunda posição.

import ast

def selection_sort(vetor, inicio = 0):

    if inicio >= len(vetor) - 1:
        return vetor

    indice_minimo = inicio

    for i in range(inicio + 1, len(vetor)):
        if vetor[i] < vetor[indice_minimo]:
            indice_minimo = i

    vetor[inicio], vetor[indice_minimo] = vetor[indice_minimo], vetor[inicio]

    return selection_sort(vetor, inicio + 1)

lista = ast.literal_eval(input())

resultado = selection_sort(lista)
print(resultado)
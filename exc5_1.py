"Calcula o determinante de uma matriz quadrada A de tamanho máximo n>=4."

def detUm(X):
    return X[0][0]

def detDois(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]

def detTres(X):
    soma1 = X[0][0]*X[1][1]*X[2][2] + X[0][1]*X[1][2]*X[2][0] + X[0][2]*X[1][0]*X[2][1]
    soma2 = X[0][0]*X[1][2]*X[2][1] + X[0][1]*X[1][0]*X[2][2] + X[0][2]*X[1][1]*X[2][0]
    return soma1 - soma2


def submatriz(matriz, j):
    return [linha[:j] + linha[j+1:] for linha in matriz[1:]]

def calcular_det(A):
    n = len(A)
    
    if n == 1:
        return detUm(A)
    elif n == 2:
        return detDois(A)
    elif n == 3:
        return detTres(A)
    
    det = 0
    for j in range(n):
        elemento = A[0][j]
        sinal = (-1) ** (0 + j)
        sub = submatriz(A, j)
        det += sinal * elemento * calcular_det(sub)
        
    return det

A = eval(input())
print(calcular_det(A))
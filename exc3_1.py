"Calcula o determinante de uma matriz quadrada A"
"de tamanho máximo n = 3."

A = eval(input())
n = len(A)

def detUm(X):
    determinante = X[0][0]
    return determinante

def detDois(X):
    determinante = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    return determinante

def detTres(X):
    soma1 = X[0][0]*X[1][1]*X[2][2] + X[0][1]*X[1][2]*X[2][0] + X[0][2]*X[1][0]*X[2][1]
    soma2 = X[0][0]*X[1][2]*X[2][1] + X[0][1]*X[1][0]*X[2][2] + X[0][2]*X[1][1]*X[2][0]
    determinante = soma1 - soma2
    return determinante

if n < 2:
    det = detUm(A)
elif 1 < n < 3:
    det = detDois(A)
else:
    det = detTres(A)

print(det)
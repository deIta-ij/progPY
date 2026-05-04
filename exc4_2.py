"Lê duas matrizes de elementos inteiros."
"Retorna a soma das matrizes."

A = eval(input())
B = eval(input())

linhasA = len(A)
linhasB = len(B)
colunasA = len(A[0])
colunasB = len(B[0])

def soma(A,B):
    if linhasA != linhasB or colunasA != colunasB:
        return 0
    else:
        C = []
        for i in range(linhasA):
            linhaC = []
            for j in range(colunasA):
                linhaC.append(A[i][j] + B[i][j])
            C.append(linhaC)
        return C
    
resultado = soma(A,B)

if resultado != 0:
    print(resultado)
else:
    print("Erro!")
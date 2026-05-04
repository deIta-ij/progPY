"Retorna um booleano informando se uma matriz é um quadrado mágico."

def quadrado_magico(A, i = 0, soma = None, diag_principal = 0, 
                    diag_secundaria = 0):
    
    n = len(A)

    if soma is None:
        soma = sum(A[0])

    if i == n:
        return diag_principal == soma and diag_secundaria == soma
    
    if sum(A[i]) != soma:
        return False
    
    soma_col = sum(A[j][i] for j in range(n))
    if soma_col != soma:
        return False
    
    return quadrado_magico(A, i + 1, soma, diag_principal + A[i][i],
                           diag_secundaria + A[i][n-1-i])

A = eval(input())

print(quadrado_magico(A))
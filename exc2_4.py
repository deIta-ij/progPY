"Decide se um vetor A é uma subsequência de um vetor B."
"Retorna True ou False."

A = eval(input())
B = eval(input())

def verificaSubsequencia(A, B):
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            i += 1
        j += 1

    return i == len(A)

print(verificaSubsequencia(A, B))
"Recebe dois vetores A e B e decide se existe um índice i tal que"
"A[i] = B[i]."

A = eval(input())
B = eval(input())

C = []

for a, b in zip(A, B):
    C.append(a == b)
    
if True in C:
    print(True)
else:
    print(False)
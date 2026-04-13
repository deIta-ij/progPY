"Lê um número inteiro não negativo n."
"Cria uma lista com todos os números da sequência de Fibonacci"
"até n. Imprime a lista em uma linha e a soma dos elementos"
"em outra."

n = int(input())

fibo = [0, 1]
soma = fibo[0]

if n < 1:
    print([fibo[0]])
    print(soma)
else:
    soma += fibo[1]
    while True:
        prox = fibo[-1] + fibo[-2]
        if prox > n:
            break
        fibo.append(prox)
        soma += prox
    print(fibo)
    print(soma)
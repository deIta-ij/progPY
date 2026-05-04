"Faz uma função lazy (geradora) que retorna a sequência de Fibonacci"
"infinita."

n = int(input())

def f_lazy_fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


for i, x in enumerate(f_lazy_fibonacci()):

    if i >= n:   
        break

    print(x, end=' ')
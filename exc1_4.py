"Produto interno de dois vetores."
"Lê dois vetores e imprime o resultado do produto interno."

v1 = eval(input())
v2 = eval(input())
produto = 0.0

for i in range(len(v1)):
    produto += v1[i] * v2[i]

print(produto)
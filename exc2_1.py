"Faz a leitura de um número."
"Aplica esse número a duas funções:"
"   Uma retorna o número de dígitos de um número inteiro "
"   não negativo."
"   Outra inverte o número."
"Imprime uma lista com o primeiro elemento sendo o número"
"de dígitos e o segundo o número invertido."

num = input()

def inverte(x):
    contra = [int(x[::-1])]
    return contra 

def tamanho(x):
    dig = [len(x)]
    return dig

resultado = tamanho(num) + inverte(num)
print(resultado)
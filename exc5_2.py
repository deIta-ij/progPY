"Função divisores() retorna um conjunto com todos os divisores de um número inteiro positivo. "
"Função intersec() recebe os dois ou mais números inteiros positivos,"
"chama a primeira função para cada um dos números obtendo os conjuntos de seus divisores."
"Calcula e retorna a interseção desses conjuntos, ou seja, os divisores comum desses números."
"Entrada uma tupla com os números. Saída um conjunto com os divisores comuns."

def divisores(n):
    j = 0
    divs = set()

    for i in range(1, n+1):

        if ( n % i == 0):
            divs.add(i)

    return divs

def intersec(*args):
    lista_de_divs = [divisores(n) for n in args]

    return set.intersection(*lista_de_divs)

nums = eval(input())

resultado = intersec(*nums)
print(resultado)
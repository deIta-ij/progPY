"Recebe uma string e imprime os seguintes itens:"
"Número de caracteres, número de letras, número de números,"
"número de símbolos e número de palavras."

frase = input()
num_char = len(frase)
num_letras = 0
num_nums = 0
num_sim = 0
num_palavras = 0

for char in frase:
    if char.isalpha():
        num_letras += 1
    elif char.isdigit():
        num_nums += 1
    else:
        num_sim += 1
        if char != "-":
            frase = frase.replace(char," ")

separa = frase.split()
palavras = []
for bla in separa:
    if bla != "-":
        palavras.append(bla)

num_palavras = len(palavras)

print(num_char, num_letras, num_nums, num_sim, num_palavras)
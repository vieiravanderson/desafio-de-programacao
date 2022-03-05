# Questão 3

import math

s = input("Digite uma mensagem para ser encriptada: ").strip()
string = s.replace(" ", "")
tamanho_string = len(string)
raiz = tamanho_string ** 0.5
linhas_colunas = math.ceil(raiz)
numero = linhas_colunas

lista = []

for c in range(len(string)):
    lista.append(string[c])

lista_de_listas = []

while numero > 0:
    for c in lista:
        if len(lista) >= linhas_colunas:
            lista_de_listas.append(lista[:linhas_colunas])
            del lista[:linhas_colunas]
        else:
            lista_de_listas.append(lista[::])
            del lista[::]
    numero -= 1

for e in lista_de_listas:
    while len(e) < linhas_colunas:
        e.append('')

n = 0
while n < linhas_colunas:
    for c in lista_de_listas:
        print(f"{c[n]}", end='')
    print(" ", end='')
    n += 1

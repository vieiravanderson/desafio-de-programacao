# Questão 3

import math

s = input("Digite uma mensagem para ser encriptada: ").strip()
string = s.replace(" ", "")
tamanho_string = len(string)
raiz = tamanho_string ** 0.5
linhas_colunas = math.ceil(raiz)
contador = 0
for i in range(linhas_colunas):
    print(f"{string[contador::linhas_colunas]}", end=' ')
    contador += 1



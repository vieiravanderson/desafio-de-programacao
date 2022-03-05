# Questão 2

tamanho_do_vetor = int(input("Informe o tamanho do vetor: "))
vetor = []
for c in range(tamanho_do_vetor):
    elemento = int(input(f"Digite o {c + 1}º elemento do vetor: "))
    vetor.append(elemento)

print(f"vetor = {vetor}")
x = int(input("Agora digite um número inteiro qualquer x: "))
pares_de_elementos = 0
lista_de_pares = []

for n in vetor:
    y = n - x
    if y in vetor:
        pares_de_elementos = pares_de_elementos + 1
        lista_de_pares.append([n, y])

if pares_de_elementos == 0:
    print(f"Não existem pares de elementos no vetor com uma diferença de {x}")
else:
    print(f"Existe(m) {pares_de_elementos} par(es) de elementos no vetor com uma diferença  de {x}: {lista_de_pares}")

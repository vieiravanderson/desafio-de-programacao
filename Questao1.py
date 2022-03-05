# Questão 1

lista = []
tamanho = int(input("Informe quantos elementos você deseja ter em sua lista(precisa ser um número ímpar): "))
tamanho_par = True

if tamanho % 2 == 0:
    while tamanho_par:
        tamanho = int(input("Você informou um valor par. Por favor, digite um valor ímpar: "))
        if tamanho % 2 != 0:
            tamanho_par = False

for i in range(tamanho):
    elemento = int(input(f"Digite o {i + 1}º elemento da lista: "))
    lista.append(elemento)

print(f"Sua lista: {lista}")

lista.sort()
posicao_meio = len(lista) // 2
mediana = lista[posicao_meio]
print(f"A mediana da sua lista é: {mediana}")

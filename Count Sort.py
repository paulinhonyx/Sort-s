def count_sort(lista):
    contagem = [0 for i in range(max(lista) + 1)]

    for i in lista:
        contagem[i] += 1

    for indice in range(1, len(contagem)):
        contagem[indice] = contagem[indice - 1] + contagem[indice]

    L = [0 for loop in range(len(lista))]
    for i in lista:
        indice = contagem[i] - 1
        L[indice] = i
        contagem[i] -= 1

    return L


def gerar(int):
    from random import randint
    tamanho = int
    lista = [0] * tamanho

    for i in range(tamanho):
        lista[i] = randint(0, 1000)

    print("Lista não ordenada:", lista, "\n")
    return count_sort(lista)


print("Qual o tamanho do vetor:\n")
vetor = int(input())
print("Lista ordenada:", gerar(vetor))

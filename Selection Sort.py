def selection_sort(lista):
    elementos = len(lista) - 1
    comparacoes = 0

    for j in range(elementos):
        minimo = j
        for i in range(j + 1, elementos + 1):
            if lista[i] < lista[minimo]:
                minimo = i
                comparacoes += 1
            comparacoes += 1
        lista[j], lista[minimo] = lista[minimo], lista[j]

    print("Lista ordenada:", lista)
    print("comparações:", comparacoes)
    return lista


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 100)

    print("Lista não ordenada:", resposta, "\n")
    return selection_sort(resposta)


print("Qual o tamanho do vetor:")
vetor = int(input())
gerar(vetor)

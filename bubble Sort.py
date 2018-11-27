def bubble_sort(lista):
    elementos = len(lista) - 1
    ordenado = False
    comparacoes = 0
    while not ordenado:
        ordenado = True

        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
                # print(lista,"\n")
            comparacoes += 1

    print("Lista ordenada:", lista)
    print("comparaçoes:", comparacoes)
    return lista


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 100)

    print("Lista não ordenada:", resposta, "\n")
    return bubble_sort(resposta)


print("Qual o tamanho do vetor:\n")
vetor = int(input())
gerar(vetor)

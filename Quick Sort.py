def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    if len(lista) > 1:
        pivo = lista[0]
        equal = [x for x in lista if x == pivo]
        lesser = [x for x in lista if x < pivo]
        greater = [x for x in lista if x > pivo]
        # print(lista)
        return quick_sort(lesser) + equal + quick_sort(greater)
    print(lista)


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 100)

    print("Lista não ordenada:", resposta, "\n")
    return quick_sort(resposta)


print("Qual o tamanho do vetor:\n")
vetor = int(input())
print("Lista ordenada:", gerar(vetor))

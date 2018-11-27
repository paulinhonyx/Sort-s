comp = 0


def max_heapfy(lista, raiz, tamanho):
    esq = 2 * raiz + 1
    dir = 2 * raiz + 2
    maior = raiz
    global comp
    if esq < tamanho and lista[esq] > lista[raiz]:
        maior = esq
        comp += 1
    if dir < tamanho and lista[dir] > lista[maior]:
        maior = dir
        comp += 1
    if maior != raiz:
        lista[maior], lista[raiz] = lista[raiz], lista[maior]
        max_heapfy(lista, maior, tamanho)
        comp += 1


def heap_sort(lista):
    n = len(lista)
    global comp
    for i in range(n // 2, -1, -1):
        max_heapfy(lista, i, n - 1)
        comp += 1
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        max_heapfy(lista, 0, i)
        comp += 1
    print("Lista ordenada:", lista)
    print("Comparações:", comp)
    return lista


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 100)

    print("Lista não ordenada:", resposta, "\n")
    return heap_sort(resposta)


print("Qual o tamanho do vetor:")
vetor = int(input())
gerar(vetor)

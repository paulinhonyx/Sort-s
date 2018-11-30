comp = 0
cont = 0


def max_heapfy(lista, raiz, tamanho):
    esq = 2 * raiz + 1
    dir = 2 * raiz + 2
    maior = raiz
    global comp
    if esq < tamanho and lista[esq] > lista[raiz]:
        maior = esq
    if dir < tamanho and lista[dir] > lista[maior]:
        maior = dir
    if maior != raiz:
        lista[maior], lista[raiz] = lista[raiz], lista[maior]
        max_heapfy(lista, maior, tamanho)
    comp += 1


def heap_sort(lista):
    n = len(lista)
    global comp
    for i in range(n // 2, -1, -1):
        max_heapfy(lista, i, n - 1)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        max_heapfy(lista, 0, i)
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
print("1 - 5\n2 - 10\n3 - 100\n4 - 1000\n5 - 10000\n")
vetor = int(input())
while vetor < 1 or vetor > 5:
    print("Opção invalida.")
    print("Qual o tamanho do vetor:")
    print("1 - 5\n2 - 10\n3 - 100\n4 - 1000\n5 - 10000\n")
    vetor = int(input())
if vetor == 1:
    vetor = 5
elif vetor == 2:
    vetor = 10
elif vetor == 3:
    vetor = 100
elif vetor == 4:
    vetor = 1000
else:
    vetor = 10000
for x in range(51):
    cont += comp
    comp = 0
    gerar(vetor)
    print("-" * 100)
print("Media de comparações:", cont / 50)

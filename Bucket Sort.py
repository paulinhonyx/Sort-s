def inserir(elemento, newLista):
    if len(newLista) == 0:
        newLista.append(elemento)
        return newLista

    for i in range(len(newLista)):
        if elemento < newLista[i]:
            newLista.insert(i, elemento)
            return newLista

    newLista.append(elemento)
    return newLista


def insertion_sort(lista):
    if type(lista) != list:
        return

    newLista = []

    while len(lista) != 0:
        elemento = lista.pop()
        newLista = inserir(elemento, newLista)

    return newLista


def bucket_sort(lista, num_buckets):
    if type(lista) != list or type(num_buckets) != int:
        return
    if len(lista) < 2:
        return lista

    buckets = []
    for i in range(num_buckets):
        buckets.append([])
    bucketnum = 0
    for i in lista:
        buckets[bucketnum].append(i)
        bucketnum += 1
        if bucketnum == num_buckets:
            bucketnum = 0

    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    combined_array = []
    for i in range(num_buckets):
        for elemento in buckets[i]:
            combined_array.append(elemento)

    combined_array = insertion_sort(combined_array)
    print("Lista ordenada:", combined_array)


def gerar(int):
    from random import randint
    tamanho = int
    lista = [0] * tamanho

    for i in range(tamanho):
        lista[i] = randint(0, 1000)

    print("Lista não ordenada:", lista, "\n")
    return bucket_sort(lista, 50)


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
for x in range(50):
    gerar(vetor)
    print("-" * 100)

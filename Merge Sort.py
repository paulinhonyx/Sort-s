def merge_sort(lista):
    comp = 0
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1

            else:
                lista[k] = R[j]
                j += 1

            comp += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
            comp += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
            comp += 1

    if len(lista) == vetor:
        print("Lista ordenada:", lista)
        print("Comparações:", comp)

    return lista


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 1000000)

    print("Lista não ordenada:", resposta, "\n")
    return merge_sort(resposta)


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
for x in range(1, 50):
    gerar(vetor)
    print("-" * 100)

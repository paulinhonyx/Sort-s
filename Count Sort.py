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
    print("Lista ordenada:", gerar(vetor))
    print("-" * 100)

from math import log10


def get_digi(numero, base, pos):
    return (numero // base ** pos) % base


def prefix_sum(lista):
    for i in range(1, len(lista)):
        lista[i] = lista[i] + lista[i - 1]
    return lista


def radix_sort(l, base=10):
    passes = int(log10(max(l)) + 1)
    saida = [0] * len(l)
    for pos in range(passes):
        cont = [0] * base
        for i in l:
            digi = get_digi(i, base, pos)
            cont[digi] += 1
        cont = prefix_sum(cont)

        for i in reversed(l):
            digi = get_digi(i, base, pos)
            cont[digi] -= 1
            nova_pos = cont[digi]
            saida[nova_pos] = i

        l = list(saida)
    return saida


def gerar(int):
    from random import randint
    tamanho = int
    lista = [0] * tamanho

    for i in range(tamanho):
        lista[i] = randint(0, 1000)

    print("Lista não ordenada:", lista, "\n")
    return radix_sort(lista)


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

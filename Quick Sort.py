def quick_sort(lista):
    global comp
    if len(lista) <= 1:
        return lista

    if len(lista) > 1:
        pivo = lista[0]
        equal = [x for x in lista if x == pivo]
        lesser = [x for x in lista if x < pivo]
        greater = [x for x in lista if x > pivo]
        comp += 1
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
    comp = 0
    print("Lista ordenada:", gerar(vetor), "\n")
    print("Comparações:", comp)
    print("-" * 100)

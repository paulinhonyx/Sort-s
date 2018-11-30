def insertion_sort(lista):
    elementos = len(lista)
    comparacoes = 0

    for j in range(1, elementos):
        pivo = lista[j]
        i = j - 1

        while (i > -1) and pivo < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1
            comparacoes += 1

        lista[i + 1] = pivo
    print("comparações:", comparacoes)
    return lista


def gerar(int):
    from random import randint
    tamanho = int
    resposta = [0] * tamanho

    for i in range(tamanho):
        resposta[i] = randint(0, 100)

    print("Lista não ordenada:", resposta, "\n")
    return insertion_sort(resposta)


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
    print("Lista ordenada:",gerar(vetor))
    print("-" * 100)

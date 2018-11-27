def insertion_sort(lista):
  elementos = len(lista)
  comparacoes = 0

  for j in range(1, elementos):
    pivo = lista[j]
    i = j - 1

    while (i > -1) and pivo < lista[i]:
      lista[i + 1] = lista[i]
      i-= 1
      comparacoes+= 1
      print(lista)

    lista[i + 1] = pivo
  print(lista)
  print("comparações:", comparacoes)
  return lista


def gerar(int):

  from random import randint
  tamanho = int
  resposta = [0] * tamanho

  for i in range(tamanho):
    resposta[i] = randint(0, 100)

  print("Lista não ordenada:",resposta,"\n")
  return insertion_sort(resposta)

print("Qual o tamanho do vetor:\n")
vetor = int(input())
gerar(vetor)

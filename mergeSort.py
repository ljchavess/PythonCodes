# -*- coding: utf-8 -*-

# autor: Luan Junior Chaves
# e-mail: luanjchaves@gmail.com

#Algoritmo que faz ordenação dos valores de uma lista de numeros aleatórios

import sys

def merge(lista, aux, esquerda, meio, direita):
    for k in range(esquerda, direita + 1):
        aux[k] = lista[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            lista[k] = aux[j]
            j += 1
        elif j > direita:
            lista[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            lista[k] = aux[j]
            j += 1
        else:
            lista[k] = aux[i]
            i += 1

def mergesort(lista, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2
    mergesort(lista, aux, esquerda, meio)# Ordena a primeira metade do arranjo.
    mergesort(lista, aux, meio + 1, direita) # Ordena a segunda metade do arranjo.
    merge(lista, aux, esquerda, meio, direita) # Combina as duas metades ordenadas anteriormente.

lista = []
arquivo = open(sys.argv[1], "r") #abre o arquivo a ser ordenado em modo de leitura
for num in arquivo:#adiciona todos os elementos do arquivo em uma lista
    lista.append(int(num))

aux = [0]*len(lista)
mergesort(lista, aux, 0, len(lista)-1)
nomeArqOrdenado = sys.argv[1].strip(".txt")
nomeArqOrdenado = (nomeArqOrdenado+"Ord.txt")
arquivOrd = open(nomeArqOrdenado, "w")
for valor in lista:
    arquivOrd.write(str(valor)+"\n")

arquivo.close()
arquivOrd.close()

# -*- coding: utf-8 -*-

# autor: Luan Junior Chaves
# e-mail: luanjchaves@gmail.com

#Algoritmo que gera N códigos aleatórios e não repetidos composto por 32 caracteres
#   entre letras maiusculas e numeros e os salva em um arquivo 'codigos.txt'
import string
import random
import sys

parametro = int(sys.argv[1])
name_arq = "codigo.txt"
arquivo = open(name_arq, 'w')
lista = []
size=32
chars=string.ascii_uppercase + string.digits

for i in range(parametro):
    codigo = ''.join(random.choice(chars) for _ in range(size)) #gera código aleatório
    if codigo not in lista: #verifica se ele já existe na lista
        arquivo.write(str(codigo)+"\n") #grava código gerado em um arquivo
        lista.append(codigo)

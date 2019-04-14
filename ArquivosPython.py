#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:43:25 2019
Treinamento Python
@author: ale
"""

import numpy as np
import urllib.request as rq
from random import choice
import pdb as pd
from random import randint
import csv
'''
Comando whie é ineficiente em 
python
'''
''' a = 10
print(type(a))

a = (1, 2, 3, 4)
lista = [2,3,4,5,6,7, "Valor"]
for i, x in enumerate(lista):
  print(i, "->", x)
print(type(lista))
print(type(a))

lista = lista + [8]
print(lista[-1:-3:-2])
print(len(lista))
print(lista[len(lista) - 1])

#Primeiro exercício
#Primeira Forma
lista = np.array([2,3,4,5,6,7])
lst = lista * lista
print(lst)

#Segunda Forma
def quadrado(x):
  return x*x
list = [quadrado(x) for x in lista]
print(list)

#Dicionários
Dict = {'Primeiro': 10, 'Segundo': 5}
print(type(Dict))
print(Dict.items())
print(Dict.keys())
print(Dict.values())

for itens, valores in Dict.items():
  print("Items:", itens, "Valores", valores)
 '''

# Terceiro Exercício
url = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
response = rq.urlopen(url)
texto = response.read().decode()
palavras = texto.splitlines()
#pd.set_trace()

class Erro(Exception):
  def __str__(self):
    print("Divisao por numero nao par! (Nao e possivel colocar apenas nome)")

def GetNome(a, tamanho):
  index = 0
  while index < tamanho:
    intermed = choice(palavras)
    if intermed[0].isupper():
      bol = True
      for index2 in range(1, len(intermed)):
        if intermed[index2].isupper():
          bol = False
          break
      if bol == True:
        a.append(intermed)
        index = index + 1

def Print(a, tamanho):
  half = int(tamanho/2)
  for index in range(0, half):
    #pd.set_trace()
    print("Primeiro Nome:", a[index], "Ultimo Nome:", a[half + index - 1])

def Divide(a, tamanho):
  c = []
  d = []
  e = []
  half = int(tamanho/2)
  for index in range(0, half):
    c.append(a[index])
    d.append(a[half + index - 1])
    e.append(a[index] + " " + a[half + index - 1])
  return c,d, e

try:
  tamanho = 20
  if tamanho % 2 != 0:
    raise(Erro)
except Erro():
  print("Erro")


a = []
GetNome(a, tamanho)
Print(a, tamanho)
[Nome, Sobrenome, NomeCompleto] = Divide(a, tamanho)

Boletim = {}
Boletim['NomeCompleto'] = NomeCompleto 
NUSP = [randint(10**7, 10**8) for i in NomeCompleto]
Boletim['NumeroUSP'] =  NUSP
notas = [randint(1,5) for i in NomeCompleto]
Boletim['Nota']  = notas
Classificacao1 = ['Pessimo', 'Ruim', 'Bom', 'Muito Bom', 'Excelente']
Classificacao2 = [{index1 + 1: index2} for index1, index2 in enumerate(Classificacao1)]
Boletim['Classificacao'] = [Classificacao2[index - 1] for index in notas]

print(Boletim['Classificacao'])

'''
Criar aual.csv

'''
with open('aula.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['NomeCompleto','NumeroUSP', "Nota", "Classificacao"])
  for index in range(10):
    writer.writerow([Boletim['NomeCompleto'][index], Boletim['NumeroUSP'][index], Boletim['Nota'][index], Boletim['Classificacao'][index][Boletim['Nota'][index]]])




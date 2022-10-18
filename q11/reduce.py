#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
count = 1
atual_palavra = None
cidades = list()
qt_ae = list()
maior = 0
try:
  for x in sys.stdin:
    words = x.split(";")
    if atual_palavra == words[0]:
      count = count + 1
    else:
      cidades.append(atual_palavra)
      qt_ae.append(count)
      atual_palavra = words[0]
      count = 1
  
  for x in range(len(cidades)):
    if qt_ae[x] > qt_ae[maior]:
      maior = x
  
  print("{} {}".format(cidades[maior],qt_ae[maior]))
    
    
except Exception as e:
  raise(e)

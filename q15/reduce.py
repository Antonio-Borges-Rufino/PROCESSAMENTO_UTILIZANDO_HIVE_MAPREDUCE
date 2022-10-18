#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
paises = list()
pais_atual = None
try:
  for x in sys.stdin:
    if pais_atual == x:
      pass
    else:
      paises.append(x)
      pais_atual = x
  print(len(paises)-1)
    
except Exception as e:
  raise(e)

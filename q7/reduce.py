#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
alt = list()
try:
  for x in sys.stdin:
    alt.append(x)
  maior = float(alt[1].replace('\t\n',''))
  menor = float(alt[0].replace('\t\n',''))
  print(maior-menor)
except Exception as e:
  raise(e)

#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
name = None
atual_alt = 0
try:
  for x in sys.stdin:
    words = x.split(";")
    altitude = float(words[1].replace("/t/n",""))
    if altitude > atual_alt:
      atual_alt = altitude
      name = words[0]
  print(name)
    
except Exception as e:
  raise(e)

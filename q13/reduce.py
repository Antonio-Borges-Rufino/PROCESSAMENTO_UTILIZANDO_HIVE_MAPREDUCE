#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
name = None
altitude = 0
count = 0
try:
  for x in sys.stdin:
    #words = x.split(";")
    altitude = altitude + float(x)
    count = count + 1
  print(altitude/count)
    
except Exception as e:
  raise(e)

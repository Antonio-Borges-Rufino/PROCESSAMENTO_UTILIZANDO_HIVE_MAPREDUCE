#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
dst = list()
try:
  for x in sys.stdin:
    words = x.split(',')
    #if words[3]!=" "
    print("{}".format(words[3])) 

except Exception as e:
  raise(e)


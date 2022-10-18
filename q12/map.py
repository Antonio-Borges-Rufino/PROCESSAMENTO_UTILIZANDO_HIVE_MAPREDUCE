#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
try:
  for x in sys.stdin:
    words = x.split(',')
    #if words[3] == '\"Brazil\"':
    if words[1] != '\"\"':
      print('{};{}'.format(words[1],words[8]))
except Exception as e:
  raise(e)


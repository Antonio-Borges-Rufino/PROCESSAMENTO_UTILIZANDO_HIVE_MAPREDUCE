#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
try:
  for x in sys.stdin:
    words = x.split(',')
    if words[1] == '\"Jorge Newbery Airpark\"':
      print('{}'.format(words[8]))
    if words[1] == '\"Altamira Airport\"':
      print('{}'.format(words[8]))
except Exception as e:
  raise(e)


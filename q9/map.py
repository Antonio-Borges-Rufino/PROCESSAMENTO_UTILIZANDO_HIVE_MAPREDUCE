#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
try:
  for x in sys.stdin:
    words = x.split(',')
    if words[3] == '\"Brazil\"':
      print('{}'.format(1))
except Exception as e:
  raise(e)


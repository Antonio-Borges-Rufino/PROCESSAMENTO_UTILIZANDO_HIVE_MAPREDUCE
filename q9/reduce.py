#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
count = 0
try:
  for x in sys.stdin:
    count = count + 1
  print(count)
except Exception as e:
  raise(e)

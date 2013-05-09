#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Interpolación: Taylor
# Gabriela Balcedo Acosta y Vanesa Abad Armas
# Curso: 2012/2013
from math import *
from sympy import *

A=0
B=2
def factorial(n):
    if (n<2):
         return 1
    r=1
    for i in range(2,n+1):
      r*=i
    return r
def deriv():
  symb_x = Symbol('x')
  func = (5**symb_x)

  derivada = diff(func, symb_x, a)
  x = 1.5
  print derivada
  print "El resultado de evaluar la derivada {0}-esima en el punto {1} es {2}".format(a, x, eval(str(derivada)))

if __name__ == "__main__":
  a=int(raw_input("¿Hasta que termino decea obtener?"))
  n=int(raw_input("Introduce n"))
  j=0
  p=0
  while p < a:
    while j< a:
      taylor= (5**0+(B-A)**j+1/factorial(n))*(deriv())
    j+=1
  p+=1
  print taylor



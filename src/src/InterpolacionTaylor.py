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
  x=1.5
  
if __name__ == "__main__":
  a=int(raw_input("¿De cuantos pasos quiere la serie?")) 
  j=0
  for j in range(a):
    n=int(raw_input("Introduce el factorial"))
    for i in range(a):
      taylor=((5**1.5)+(B-A)/factorial(n))*deriv()
  j+=1
  #print derivada
  #print "El resultado de evaluar la derivada {0}-esima en el punto {1} es {2}".format(n, x, eval(str(derivada)))
  print "La evaluación es:",taylor


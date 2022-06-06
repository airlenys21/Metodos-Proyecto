from matplotlib import pyplot
from sympy import *
from math import *
import sympy as sp
import numpy as np
# Algoritmo Posicion Falsa para raices
# busca en intervalo [a,b]
# INGRESO  -0.5*(x**2) + 2.5*x + 4.5  5  10

x = Symbol('x')
fx = parse_expr(input("ingresa la ecuación: "))
a = parse_expr(input("ingresa punto de intersección 1: "))
b = parse_expr(input("ingresa punto de intersección 2: ")) 


tolera = 0.001

# PROCEDIMIENTO
tramo = abs(b-a)
while not(tramo<=tolera):
    fa = fx.subs(x,a)
    fb = fx.subs(x,b)
    c =float( b - fb*(a-b)/(fa-fb))
    fc = fx.subs(x,c)
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia > 0):
        tramo = abs(c-a)
        a = c
    else:
        tramo = abs(b-c)
        b = c
raiz = c

# SALIDA
print(raiz)



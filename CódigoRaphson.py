# Método de Newton-Raphson
#Ejemplo x**3-4*x**2-2  ; Intersección 4
from sympy import *
from math import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#Ingreso de la función
x = Symbol('x')
fx=parse_expr(input("Ingrese el fx: "))
xi= parse_expr(input("Mete la Intersección: "))


#Resolver derivada

y = fx

derivada = sp.diff(y,x) 
print('Derivada la es:', derivada) #Se imprime la derivada

# PROCEDIMIENTO

tolera = 0.001
tramo = abs(2*tolera)
while (tramo >= tolera):
    
    #Reemplazar la x por la intersección en la funcion
    fxx  = fx.subs(x,xi)

    #Reemplazar la x por la intersección en la derivada
    dfx = derivada.subs(x,xi)

    #Calcula el siguiente estimado de la solución
    xnuevo = float(xi) - float(fxx / dfx)

    tramo  = abs(xnuevo-xi)
    xi = xnuevo

# SALIDA
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)

print('raiz en: ', xi)
print('con error de: ',tramo)

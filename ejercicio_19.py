# Resolver una ecuación cuadrática Escribe un programa que resuelva
#  una ecuación cuadrática de la forma ax^2 + bx + c = 0, donde a, b, y c son números proporcionados 
# por el usuario. El programa debe devolver las soluciones de la ecuación utilizando la fórmula cuadrática.

import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None  # No tiene soluciones reales

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

soluciones = resolver_ecuacion_cuadratica(a, b, c)

if soluciones:
    print(f"Las soluciones son: {soluciones}")
else:
    print("La ecuación no tiene soluciones reales.")

# Este programa sirve para calcular Series de Fourier Discretas
# Autor: Uriel ALvarez
# Fecha: 30 de abril de 2023

"""
En este código se usa la formula de una Senosoide, se usan librerias matplotlib y numpy

Imprime una expresión matemática de forma agradable utilizando la biblioteca SymPy.

"""

#importo las librerias
from sympy import symbols, sin, cos, pprint

# Crear los símbolos
t = symbols('t')
A_0 = symbols('A₀')
A_1 = symbols('A₁')
B_1 = symbols('B₁')
w_0 = symbols('w'+'\u2080')


# Crear una expresión de función
expr = A_0 + A_1 * cos(w_0 * t) + B_1 * sin(w_0 * t)

# Imprimir la expresión de forma agradable
pprint(expr)





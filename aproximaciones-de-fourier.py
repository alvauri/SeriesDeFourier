# Este programa sirve para calcular Series de Fourier Discretas
# Autor: Uriel ALvarez
# Fecha: 30 de abril de 2023

"""
En este código se usa la formula de una Senosoide, se usan librerias matplotlib y numpy

Imprime una expresión matemática de forma agradable utilizando la biblioteca SymPy.

El proposito de esté código es:
Llevar está expresión A₀ + A₁⋅cos(t⋅w₀) + B₁⋅sin(t⋅w₀)
a esta 
"""

#importo las librerias
from sympy import symbols, sin, cos, pprint

# Crear los símbolos para la primera formula  A₀ + A₁⋅cos(t⋅w₀) + B₁⋅sin(t⋅w₀)
t = symbols('t')
A_0 = symbols('A₀')
A_1 = symbols('A₁')
B_1 = symbols('B₁')
w_0 = symbols('w'+'\u2080')

# Crear los símbolos adicionales que faltan para la segunda formula C₁ y θ
C_1 = symbols('C\u2081')
o = symbols('\u03b8')

# Crear una expresión de función para la  A₀ + A₁⋅cos(t⋅w₀) + B₁⋅sin(t⋅w₀)
expr = A_0 + A_1 * cos(w_0 * t) + B_1 * sin(w_0 * t)

#Crear una espresión de función para la segunda formula
expr2 =  A_0 + C_1 * cos(w_0 * t + o)



# Imprimir las expresiones de forma agradable
pprint(expr)
pprint(expr2)





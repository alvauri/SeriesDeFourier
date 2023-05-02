# Este programa sirve para calcular Series de Fourier Discretas
# Autor: Uriel Alvarez
# Fecha: 1 de Mayo de 2023

"""
El proposito de este código es siplemente crear una función que muestre por pantalla
las formulas que se van a usar de forma amigable es decir en formato matematico

"""

#Importar las librerias
from sympy import symbols, sin, Eq, cos, sqrt, pprint

def mostrar_ecuaciones():
    # Crear los símbolos y expresiones
    t = symbols('t')
    A_0 = symbols('A₀')
    A_1 = symbols('A₁')
    B_1 = symbols('B₁')
    w_0 = symbols('w'+'\u2080')
    C_1 = symbols('C\u2081')
    o = symbols('\u03b8') # o va representar la letra griega teta

    # Expresiones para mostrar las funciones
    expr = A_0 + A_1 * cos(w_0 * t) + B_1 * sin(w_0 * t)
    expr2 = A_0 + C_1 * cos(w_0 * t + o)

    # Expresiones para mostrar las formulas
    C_1_eq = Eq(C_1, sqrt(A_1**2 + B_1**2))
    o_eq = Eq(o, ((-1) * B_1) / A_1)
    
    # Imprimir las expresiones de forma agradable
    print('\033[1mEXPLICACIÓN\033[0m') #Es una forma de mostrar un texto en negrita
    print("-Partimos de este tipo de función")
    pprint(expr)
    print('')
    print('-Queremos expresarla de esta forma')
    pprint(expr2)
    print('-Usamos estas formulas:')
    pprint(C_1_eq)
    print('')
    pprint(o_eq)
    print('Nota: Tener encueta que si A₁ es negativo hay que sumarle \u03c0 al periodo que obtuve')
    
    

# Este seria el programa principal
# Llamar a la función para mostrar las ecuaciones
mostrar_ecuaciones()

# Este programa sirve para calcular Series de Fourier Discretas
# Autor: Uriel ALvarez
# Fecha: 30 de abril de 2023

"""
En este programa me enseño a usar librerias como Sympy para mostrar simbolos matemáticos
por pantalla.
Tambien usamos una libreria para visualizar graficar: Matplotlib

"""
import matplotlib.pyplot as plt
import numpy as np

# Crear un array de valores x
x = np.linspace(-10, 2*np.pi, 200)

# Calcular los valores de la función seno
y = np.sin(x)

# Agregar línea del eje y en 0
plt.axhline(y=0, color='blue', linewidth=1.5)

# Agregar línea vertical en x=0
plt.axvline(x=0, color='blue', linewidth=1.5)

# Graficar la función seno
plt.plot(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Ajustar los límites del eje x
plt.xlim(-2*np.pi, 2*np.pi)

# Agregar un cartel dentro del gráfico
plt.text(0, 1, 'Grafica de Seno de x', ha='center', va='center', fontsize=12)

# Mostrar el gráfico
plt.show()
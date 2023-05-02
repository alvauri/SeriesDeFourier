# Este programa sirve para calcular Series de Fourier Discretas
# Autor: Uriel ALvarez
# Fecha: 30 de abril de 2023

"""
Este código grafica la función coseno en un rango de valores x desde -10 hasta 2π, 
y muestra el eje y en 0 y el eje x en 0.

El gráfico incluye etiquetas para los ejes x e y, con 'x' 
como etiqueta para el eje x y 'cos(x)' como etiqueta para el eje y.

Además, se agrega un cartel dentro del gráfico con el texto 
"Grafica de coseno de x" ubicado en el centro del gráfico.

Para ejecutar el código y mostrar el gráfico, utiliza el método plt.show().

Recuerda que puedes ajustar los valores de los parámetros 
según tus necesidades y preferencias.

En este programa se usan librerias matplotlib y numpy.
"""
import matplotlib.pyplot as plt
import numpy as np

# Crear un array de valores x
x = np.linspace(-10, 2*np.pi, 200)

# Calcular los valores de la función coseno
y = np.cos(x)

# Agregar línea del eje y en 0
plt.axhline(y=0, color='blue', linewidth=1.5)

# Agregar línea vertical en x=0
plt.axvline(x=0, color='blue', linewidth=1.5)

# Graficar la función coseno
plt.plot(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('x')
plt.ylabel('cos(x)')

# Ajustar los límites del eje x
plt.xlim(-2*np.pi, 2*np.pi)

# Agregar un cartel dentro del gráfico
plt.text(0, 1, 'Grafica de Coseno de x', ha='center', va='center', fontsize=12)

# Mostrar el gráfico
plt.show()
"""
Autor: Uriel Alvarez
Nombre: Ajuste de métodos cuadrados a una sinusoide usando Python
Version: 1.0
Propósito: El propósito del presente código es escribir un programa en python que se encargue de hacer lo siguiente:
Objetivos Primarios:
- Que tome los parametros de la función calcule y genere los valores de la tabla aplicando el método
- Muestre los resultados en forma clara

Objetivos secundarios:
- Mostrar de una forma más amigable los resultados y que la tabla exportarla a .CSV
- También pensé que una vez generada el archivo .csv lo suba directamente a una carpeta de Google Drive

Librerias que considero que serán necesarias:
En primera instancia para cubrir los objetivos primarios deberiamos usar Pandas
Para los objetivos secundarios deberiamos usar Sympy y PyDrive la primera sirve para que se vean las formulas de forma más amigable
y el segundo sirve para poder conectar el programa con Drive.

"""

# Importamos las librerias necesarias pandas, numpy, etc
import pandas as pd
import numpy as np
# Este es un ejemplo de la estructura de la tabla que pienso hacer 
# una tabla con cuatro columas 
""" data = {
    't' : [1],
    'y' : [2],
    'ycos' : [3],
    'ysen' : [2]
} """

# Para un calculo rapido aquí voy a definir las variables
""" w0 =


 """# Creamos un DataFrame
df = pd.DataFrame()

# Generamos los valores de la columna t
# Notar que aquí quiero genere el valor 360 incluido debemos poner como limite superior un valor ligeramente más grande de otra forma no incluiria ese valor (es para asegurarnos qu elo incluya)
t_values = np.arange(0, 1.35, 0.15)  

# Asignamos los valores generados a la comuna 't' en el DataFrame
df['t'] = t_values

# Ahora calculo los valores del la columna y que en mi caso representara a la función y
w0 = 4.18
y_values = 1.7 + 0.5 * np.cos(w0 * df['t']) - 0.866 * np.sin(4.18 * df['t'])

# A continuación voy a truncar en la tercer cifra significativa es una forma debe haber otra manera de hacerlo
y_values_truncated = np.trunc(y_values * 1000) / 1000

# Ahora asigno los mismos valores pero truncados a la tercer cifra significativa
df['y'] = y_values_truncated


# Ahora hacemos lo mismo para las dos columnas faltantes 'ycos' y 'ysen'
# Calculamos los valores de las columnas
ycos_value = df['y'] * np.cos(w0 * df['t'])
ysen_value = df['y'] * np.sin(w0 * df['t'])

# Asignamos los valores truncados a la tercer cifra significativa
df['ycos'] = np.trunc(ycos_value * 1000) / 1000  
df['ysen'] = np.trunc(ysen_value * 1000) / 1000


# Mostramos en pantalla 
print(df.to_string(index=False))

# Asi generamos un archivo CSV que luego se guardará una carpeta especifica de mi escritorio
ruta = r'C:\Users\Pablo Uriel Alvarez\Desktop\Repositorio_csv/datos.csv'
df.to_csv(ruta, index=False)
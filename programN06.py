# Dropping Rows and Columns in pandas Dataframe
"""Fuente:
https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
"""

import pandas as pd

print("Creamos el DataFrame 'df':")
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Choice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(df)
print("\n")
print("Ahora borramos las filas 'Choice' y 'Pima':")
print(df.drop(['Choice', 'Pima']))
print("\n")
print("Borrar una variable (columna)")
print(df.drop('reports', axis=1))
print("Borrar una fila si esta contiene cierto valor (en este caso 'Tina'")
print("\n")
print(df[df.name != 'Tina'])
print("\n")
print("Borrar una fila por su número de posición")
print(df.drop(df.index[2]))
print("\n")
print("Borrar haciendo un rango")
print(df.drop(df.index[[2,3]]))
print("\n")
print("Borrando el final relativo para las filas")
print(df.drop(df.index[-2]))
print("\n")
print("Nuestro 'df' era:")
print(df)
print("Se puede seleccionar rangos relativos de la parte superior ")
print(df[:3])
print("Se puede seleccionar rangos relativos desde el principio hasta -3")
print(df[:-3])
print("Se puede seleccionar de atrás hacia delante")
print(df[-3:])

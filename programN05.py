"""Fuente:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html

Objetivo de Jhon: Eliminar columnas de un dataframe en función a su posición"""
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
print("DataFrame 'df'")
print(df)
print("Ahora hemos de usar 'drop' para las columnas 'B' y 'C' con un esquema 1:")
print(df.drop(['B', 'C'], axis=1))
print("Ahora hemos de usar 'drop' para las columnas 'B' y 'C' con un esquema 2:")
print(df.drop(columns=['B', 'C']))
print("Ahora hemos de usar 'drop' para las filas según su posición:")
print(df.drop([0, 1]))

print("\n")
print("Ahora 'drop' para filas o columnas múltiples de un DataFrame:")
midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2,],
                            [0, 1, 2, 0, 1, 2, 0, 1, 2]])
df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3, 0.2]])
print(df)
print("Comenzamos a borrar, la fila 'cow' con la columna 'small'")
print(df.drop(columns='small'))

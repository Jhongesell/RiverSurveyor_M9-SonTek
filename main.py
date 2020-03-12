import os
import pandas as pd
from pandas import ExcelWriter
import numpy as np
tablaN01_df = pd.read_excel('files_resources/Example_N01_V02.xlsx', '20190914090848')
df = pd.DataFrame(tablaN01_df)
a = type(tablaN01_df)
b = type(df)
print(df.head())
print("\n")
print("La variable 'tablaN01_df' es de tipo "+str(a))
print("La variable 'df' es de tipo "+str(b))
if a==b:
    print("'tablaN01' y 'df' son el mismo tipo de dato.")
print("\n")
print("Las dimensiones de la tabla son: ")
print("Total de filas: "+str(len(df.index)))
print("Total de columnas: "+str(len(df.columns)))
print("\n")
print("Purgar algunos campos de la hoja excel, quedando:")
df_N01 = df.drop(['Date/Time', 'Frequency (MHz)', 'Profile Type'], axis=1)
print(df_N01.head())
print("El tipo de datos de la variable es "+str(type(df_N01)))
df_transposed = df_N01.T
print(df_transposed.head())
df_N02 = df_transposed
#purga1 = df_N02.drop(df_N02.index[[10, 14]])
print(df_N02.drop(df_N02.index[[10, 14]]).head(16))
#print("Purgamos primeras filas innecesarias, nos interesa tener los spd")
#print(purga1[0:20])
#print("Veamos las 5 primeras filas")
#print(purga1[:20])

from seaborn import load_dataset

df = load_dataset("tips")
print("Nuestro dataframe es 'df':")
print(df.head())
"""'iloc' nos permite trabajar con filas y columnas
de un DataFrame según su posición..."""
print("Usando 'iloc':")
print(df.iloc[0:2])

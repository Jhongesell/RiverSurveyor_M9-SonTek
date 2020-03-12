from seaborn import load_dataset

df = load_dataset("tips")
print("Dataframe 'df'")
print(df.head())
"""'iloc' nos permite trabajar con filas y columnas de un DataFrame según
su posición. """
print("Usamos 'iloc':")
# sintaxis de 'iloc': data.iloc[<filas>, <columnas>]
print("Fila en la posición 0")
print(df.iloc[0]) # Primera fila
print("Fila en la posición 1")
print(df.iloc[1]) # Segunda fila
print("Fila en la última posición")
print(df.iloc[-1]) # Última fila
print("Ahora seleccionamos columnas:")
print(df.iloc[:, 0]) # Primera columna
print(df.iloc[:, 1]) # Segunda columna
print(df.iloc[:, -1]) # Última columna
print("Selección múltiple de filas o columnas mediante iloc")
print(df.iloc[0:5]) # Primeras cinco filas
print(df.iloc[:, 0:5]) # Primeras cinco columnas
print(df.iloc[[0,2,1]]) # Primera, tercera y segunda fila
print(df.iloc[:, [0,2,1]]) # Primera, tercera y segunda columna
""" Es importante tener en cuenta que 'iloc' devuelve una Serie Pandas cuando se seleeciona una fila y un DataFrame cuando se selecciona varias. EN el caso que sea necesario seleecionar un DataFrame con una única columna es necesario pasar una lista con la columna, no un escalar."""
print("Dimensiones del DataFrame: "+str(df.shape))

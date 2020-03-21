import pandas as pd
import os
tablaN01_df = pd.read_excel('files_resources/fileN01.xlsx', 'Hoja1')
df = pd.DataFrame(tablaN01_df)
a = type(tablaN01_df)
b = type(df)
print("Dataframe df")
print(df.head())
print("\n")
print("La variable 'tablaN01_df' es de tipo: "+str(a))
print("La variable 'df' es de tipo: "+str(b))
if a == b:
    print("'tablan01_DF' y 'df' son el mismo tipo de dato.")
print("\n")
print("Las dimensiones de la tabla son:")
print("Total de filas: "+str(len(df.index)))
print("Total de columnas: "+str(len(df.columns)))
print("Dataframe que eliminó la columna de 'price'")
b = df.drop(['price'], axis=1)
print("Cuadro df")
print(b)

#print("1. El tipo de dato que es df"+str(type(df)))
#invoices =  {'invoice': [1, 2],
#            'client': [4, 1]}
#invoices = pd.DataFrame(invoices)
#print("Cuadro invoices")
#print(invoices)
#print("2. El tipo de dato que es invoices"+str(type(invoices)))
#a = invoices.drop(['client'], axis=1)
#print(a)


n

"""
Convertir listas a columnas de dataframes
Fuente:
https://datatofish.com/list-to-dataframe/
"""
from pandas import DataFrame
"""
Creando un dataframe a partir de listas
"""
print("Caso 01")
your_list = ['item1', 'item2', 'item3']
df = DataFrame(your_list,columns=['Column_Name'])
print("df:")
print(df)
print("\n")
print("Caso 02")
People_List_N01 = ['Jon', 'Mark', 'Maria', 'Jill', 'Jack']
df_N01 = DataFrame(People_List_N01, columns=['First_Name'])
print("df_N01:")
print(df_N01)
print("\n")
print("Caso 03")
People_List_N02 = [['Jon', 'Smith', 21], ['Mark', 'Brown', 38], ['Maria', 'Lee', 42]]
df_N02 = DataFrame(People_List_N02, columns=['First_Name', 'Last_Name', 'Age'])
print("df_N02")
print(df_N02)
print("Transpuesta df_N02:")
df_N02_02 = DataFrame(People_List_N02).transpose()
print("df_N02_02")
print(df_N02_02)
print("People_List_N02: "+str(type(People_List_N02)))
print("df_N02_02: "+str(type(df)))
mean1 = df_N02['Age'].mean()
max1 = df_N02['Age'].max()
min1 = df_N02['Age'].min()

print("El promedio de la edad es: "+str(mean1))
print("El máximo de la edad es: "+str(max1))
print("El mínimo de la edad es: "+str(min1))

print("\n")
print("Caso 04")
People_List_N03 = [['Jon', 'Mark', 'María', 'Jill', 'Jack'],['Smith', 'Brown', 'Lee', 'Jones', 'Ford'], [21, 38, 42, 28, 55]]
df_N03 = DataFrame(People_List_N03, index = ['First_Name', 'Last_Name', 'Age'], columns = ['a', 'b', 'c', 'd', 'e'])
print(df_N03)

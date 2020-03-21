"""
Convertir listas a un dataframe

Fuente:
https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/
"""
import pandas as pd
# Creando un dataframe desde una lista
## Lista de listas
students = [['jack', 34, 'Sydeny'],
            ['Riti', 30, 'Delhi'],
            ['Aadi', 16, 'New York']]
print("Imprimiendo una lista: "+str(students))

dfObj = pd.DataFrame(students)
print("Imprimiendo mi dataframe, caso 1: "+str(dfObj))

# Creando un dataframe desde una tupla
## Lista de tuplas
students = [('Jack', 34, 'Sydeny'),
            ('Riti', 30, 'Delhi'),
            ('Aadi', 16, 'New York')]
dfObj = pd.DataFrame(students)
print("Imprimiendo mi dataframe, caso 2: "+str(dfObj))

# Creando un dataframe de una lista agregando nombreas a las columnas indexadas
## Convertir lista de tuplas a dataframe con sus respectivos nombreas para las filas y columnas
print("Imprimiendo mi dataframe, caso 3:")
dfObj = pd.DataFrame(students, columns = ['Name', 'Age', 'City'], index=['a', 'b', 'c'])
print(dfObj)
print("Imprimiendo mi dataframe, caso 4:")
# Creando dataframe desde una lista de tuplas y saltando ciertas columnas
## Creamos el dataframe desde la lista student pero saltamos la columna 'Age', solo quedan dos coulumnas
dfObj = pd.DataFrame.from_records(students, exclude=['Age'], columns = ['Name', 'Age', 'City'], index=['a', 'b', 'c'])
print(dfObj)
print("Imprimiendo mi dataframe, caso 5:")
# Creando un dataframe desde multiples lists
listOfNames = ['Jhon', 'Raquel', 'Angel']
listOfAge = [28, 26, 22]
listOfCity = ['Pomabamba', 'Lima', 'Lima']
zippedList = list(zip(listOfNames, listOfAge, listOfCity))
print(zippedList)
print("El tipo de archivo de zippedList es: "+str(type(zippedList)))
dfObj = pd.DataFrame(zippedList, columns = ['Name', 'Age', 'City'], index=['a', 'b', 'c'])
print(dfObj)

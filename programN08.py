"""Este es un programa que hace un recorrido a un index, utilizar 'range' o 'for'
"""
import numpy as np
import pandas as pd

print("Caso 01:")
x = range(6)
for n in x:
    print(n)
print("\n")
print("Caso 02:")
x = range(3, 6)
for n in x:
    print(n)
print("\n")
print("Caso 03:")
x = range(3, 20, 4)
for n in x:
    print(n)

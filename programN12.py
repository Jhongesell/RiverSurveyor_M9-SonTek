"""
Bucles anidados en Python

Fuente:
https://www.mclibre.org/consultar/python/lecciones/python-for-2.html

"""
print("CASO A")
print("Bucle de un primer nivel:")
for i in [0, 1, 2]:
    print(f"i vale {i}")
print("\n")
print("Bucle de un segundo nivel:")
for i in [0, 1, 2]:
    for j in [0, 1]:
        print(f"i vale {i} y j vale {j}")
print("\n")
print("CASO B")
print("Buble de segundo nivel:")
for i in range(3):
    for j in range(2):
        print(f"i vale {i} y j vale {j}")


print("\n")
print("CASO PRINCIPAL")
listaN01 = [1, 2]
listaN02 = [1, 2, 3]

for i in listaN01:
    for j in listaN02:
        print(f"i en listaN01 es {i} y j en listaN02 es {j}")
"""
LEER LAS COLUMNAS DE INTERES PARA CADA SET, LUEGO CONVERTIR ESAS LISTAS EN DATAFRAME
"""

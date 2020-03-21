import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from seaborn import load_dataset

print("La ruta de trabajo actual es: "+str(os.getcwd()))
tablaN01_df = pd.read_excel('files_resources/Example_N01_V02.xlsx','20190914090848')
df = pd.DataFrame(tablaN01_df)
print(df.head())

listan01 = []
listan02 = []

pos_loc_ini = 7
pos_spd_ini = 12

pos_loc_fin = len(df.columns)
pos_spd_fin = len(df.columns)

for i in range(pos_loc_ini, pos_loc_fin, 8):
    listan01.append(i)

for j in range(pos_spd_ini, pos_spd_fin, 8):
    listan02.append(j)

print("Listas 'L1' y 'L2' respectivamente son:")
print(listan01)
print(listan02)
print("Dimensiones de lista:")
print("La dimensión de L1 es "+str(len(listan01))+", mientras que de L2 es "+str(len(listan02)))



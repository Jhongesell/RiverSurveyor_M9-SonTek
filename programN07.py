import pandas as pd
from pandas import ExcelWriter

df = pd.DataFrame({'Id': [1, 3, 2, 4],
                   'Nombre': ['Juan', 'Eva', 'María', 'Pablo'],
                   'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
df = df[['Id', 'Nombre', 'Apellido']]

writer = ExcelWriter('files_ouputs/ejemplo_N01.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()

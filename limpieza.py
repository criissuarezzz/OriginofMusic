#limpieza data.csv
import pandas as pd
import numpy as np

# Cargar el archivo CSV
data = pd.read_csv('data.csv', sep=';')
#ver que columnas estan vacias, que tipo de datos tienen y cuantas filas hay, etc
print(data.info())
# Verificar si hay valores nulos en el DataFrame
print(data.isnull().sum())
# Verificar si hay valores duplicados en el DataFrame
print(data.duplicated().sum())
# Verificar si hay valores únicos en cada columna
print(data.nunique())
# Eliminar columnas innecesarias
data.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], inplace=True)

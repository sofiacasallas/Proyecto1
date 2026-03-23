import pandas as pd
import sqlite3

df=pd.read_csv('galaxias.csv')

#Se eliminan las filas que tengan al menos una casilla vacía y se toman solo paralajes positivos

df=df.dropna(subset=['Plx', 'Gmag', 'BPmag', 'RPmag'])
df=df[df['Plx']>0]

print(f"Se utilizan {len(df)} de las estrellas iniciales")

conexion = sqlite3.connect('datos_mision.db')
df.to_sql('tabla_gaia', conexion, if_exists='replace', index=False)
conexion.close()

print("Base de datos local 'datos_mision.db' esta lista.")

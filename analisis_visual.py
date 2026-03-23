import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

conexion=sqlite3.connect('datos_mision.db')

#Consuta SQL
consulta="SELECT Plx, Gmag, BPmag, RPmag FROM tabla_gaia"
df=pd.read_sql_query(consulta, conexion)
conexion.close()

#Calculos
df['color']=df['BPmag']-df['RPmag']
df['mag_abs']=df['Gmag']+5+5*np.log10(df['Plx']/1000)

#Filtros físicos post-cálculo (segunda línea de defensa)
df=df[(df['color']>=-0.5)&(df['color']<=5.5)]
df=df[(df['mag_abs']>=-5)&(df['mag_abs']<=20)]

#Graficación
fig, ax=plt.subplots(figsize=(10, 12))
scatter=ax.scatter(df['color'], df['mag_abs'],s=0.5,c=df['color'],cmap='plasma',alpha=0.7)
cbar=plt.colorbar(scatter, ax=ax)
cbar.set_label('Índice de Color BP-RP', fontsize=11)
ax.invert_yaxis()
ax.set_title('Diagrama HR - Misión Gaia DR3', fontsize=15)
ax.set_xlabel('Color (BP - RP)', fontsize=12)
ax.set_ylabel('Magnitud Absoluta (G)', fontsize=12)
ax.grid(True, alpha=0.4)
plt.tight_layout()

#Guardar imagen
plt.savefig('resultado.png')
print("La gráfica generada se encuentra como 'resultado.png'")

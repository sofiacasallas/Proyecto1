echo "Se selecciono la misión Gaia DR3 sobre evolución estelar"
wget -q -O galaxias.csv 'https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query=SELECT+TOP+50000+Source,Plx,Gmag,BPmag,RPmag+FROM+%22I/355/gaiadr3%22+WHERE+Plx%3E5'
echo "Datos descargados y guardados en galaxias.csv"
echo "Ejecutando script de bases de datos"
python3 constructor_db.py
echo "Ejecutando script de graficación"
python3 analisis_visual.py
echo "Finalizado, gráfico generado con éxito."

import pandas as pd
import os

print("Lista original")
df = pd.read_csv("Ejercicios\\trabajando_con_archivos\\datos.csv")
print(df)

#* Convertir a string los datos de la columna 'edad'
#df['Edad']=df['Edad'].astype(str)

#* Para cmbiar un dato es recomendable usar inplace en el DataFrame completo
#DALTO: df['Nombre'].replace("Cris","David",inplace=True)
#Claude:
df.replace({"Nombre": {"Cris": "David"}}, inplace=True)

#* Sobreescribir los cambios en el archivo CSV
#df.to_csv("Ejercicios\\trabajando_con_archivos\\datos.csv", index=False)

#! index=False No guarda los números de índice como una columna extra
#! Si prefieres no sobrescribir el original: 
    # df.to_csv('Ejercicios\\trabajando_con_archivos\\datos_v2.csv', index=False)

print("")
print("Lista con cambios.")

#df.dropna() # Elimina filas con datos faltantes
#df.fillna(0) # Rellena valores NaN con 0
df = df.drop_duplicates() # Elimina filas duplicadas
print(df)


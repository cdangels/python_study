#Ejercicio 2 - Gráfico de barras con ingresos mensuales por fuente

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\\graficos\\ingresos.csv")

# Crear el lineplot
sns.barplot(x="Fuente", y="Ingresos", data=df)

#Titulos y etiquetas
plt.title("Ingresos mensuales por fuente.")
plt.xlabel("Ingresos")
plt.ylabel("Fuente")

sum_ingresos = df['Ingresos'].sum()
print(f"Ingresos totales: {sum_ingresos} USD")

max_ingreso = df['Ingresos'].max() #Encontrar el valor máximo usando pandas y guardarlo en la variable max_ingreso.
max_fuente = df[df['Ingresos'] == max_ingreso]['Fuente'].iloc[0] 
'''
Esta línea primero compara la columna Ingresos con el valor máximo guardado en max_ingreso, lo que crea una máscara booleana que marca qué filas cumplen la condición. Luego aplica esa máscara al DataFrame df para quedarse solo con las filas donde el ingreso es máximo. De ese subconjunto selecciona la columna Fuente, y finalmente con .iloc[0] toma el primer valor encontrado. En pocas palabras: obtiene la fuente asociada al mayor ingreso dentro del DataFrame. '''

print(f"Ingreso máximo: {max_ingreso} USD en la fuente: {max_fuente}")

#! Eso significa que si tienes dos ingresos iguales al máximo, tu línea solo devuelve la primera “Fuente” encontrada, y las demás quedan ignoradas.

#Obtener todas las fuentes con el ingreso máximo:
max_fuentes = df[df['Ingresos'] == max_ingreso]['Fuente'].tolist()
print(f"Ingreso máximo: {max_ingreso} USD en las fuentes: {', '.join(max_fuentes)}")

plt.show( )
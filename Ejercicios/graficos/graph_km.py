#Ejercicio 1 - Gráfico de línea con kilómetros recorridos en bici a lo largo del tiempo.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\\graficos\\km_bici.csv")

sns.lineplot(x="fecha", y="km", data=df)

#! Buscar el valor más alto y marcarlo con un círculo rojo
# Método 1: Encontrar el punto máximo usando pandas
max_km = df['km'].max()
fecha_max = df[df['km'] == max_km]['fecha'].iloc[0]
print(f"Punto máximo: {max_km} km en la fecha: {fecha_max}")

# Crear el lineplot
sns.lineplot(x="fecha", y="km", data=df)

# Marcar el punto máximo con un círculo
plt.plot(fecha_max, max_km, 'ro', markersize=5)  # 'ro' = círculo rojo

#Titulos y etiquetas
plt.title("Kilómetros recorridos en bici a lo largo del tiempo")
plt.xlabel("Fecha")
plt.ylabel("Kilómetros")

plt.show( )
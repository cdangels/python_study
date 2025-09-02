import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("Ejercicios\\graficos\\km_bici.csv")

# Método 1: Encontrar el punto máximo usando pandas
max_km = df['km'].max()
fecha_max = df[df['km'] == max_km]['fecha'].iloc[0]
print(f"Punto máximo: {max_km} km en la fecha: {fecha_max}")

'''
#! Primera línea: max_km = df[' km'].max()
Esta línea busca en toda la columna 'km' del DataFrame y encuentra el valor más alto. Ese valor máximo se guarda en la variable max_km. .max es una función de pandas que devuelve el valor máximo de una serie o columna.

#! Segunda línea: fecha_max = df[df[' km'] == max_km]['fecha'].iloc[0]
Esta línea filtra todo el DataFrame para quedarse solo con las filas donde los kilómetros sean iguales al valor máximo que encontramos antes. De esas filas filtradas, toma la columna 'fecha'. Como podría haber más de una fecha con el mismo valor máximo, usa .iloc[0] para tomar solo la primera fecha encontrada. .iloc es un indexador de pandas que permite acceder a filas y columnas por posición entera.

'''

# Crear el lineplot
sns.lineplot(x="fecha", y="km", data=df)

# Marcar el punto máximo con un círculo
plt.plot(fecha_max, max_km, 'ro', markersize=5)  # 'ro' = círculo rojo

# Agregar títulos
plt.title('Kilómetros recorridos en bicicleta')
plt.xlabel('Fecha')
plt.ylabel('Kilómetros')

plt.show()

#! ===== OTRAS OPCIONES DE CÍRCULOS =====

'''
# Opción 1: Círculo más grande y personalizado
plt.figure(figsize=(10, 6))
sns.lineplot(x="fecha", y=" km", data=df)
plt.plot(fecha_max, max_km, 'ro', markersize=15, markerfacecolor='red', 
         markeredgecolor='black', markeredgewidth=2)
plt.title('Máximo marcado con círculo personalizado')
plt.show()

# Opción 2: Círculo hueco (solo el borde)
plt.figure(figsize=(10, 6))
sns.lineplot(x="fecha", y=" km", data=df)
plt.plot(fecha_max, max_km, 'ro', markersize=12, fillstyle='none', 
         markeredgewidth=3, markeredgecolor='red')
plt.title('Máximo marcado con círculo hueco')
plt.show()

# Opción 3: Usando scatter para más control
plt.figure(figsize=(10, 6))
sns.lineplot(x="fecha", y=" km", data=df)
plt.scatter(fecha_max, max_km, s=200, c='red', marker='o', 
            edgecolors='black', linewidths=2, zorder=5)
plt.title('Máximo marcado con scatter')
plt.show()

# Opción 4: Con etiqueta incluida
plt.figure(figsize=(10, 6))
sns.lineplot(x="fecha", y=" km", data=df)
plt.plot(fecha_max, max_km, 'ro', markersize=12)
plt.text(fecha_max, max_km + 1, f'{max_km} km', 
         ha='center', va='bottom', fontweight='bold')
plt.title('Máximo marcado con círculo y etiqueta')
plt.show()

'''
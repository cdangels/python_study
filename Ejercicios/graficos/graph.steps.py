#Importar las librerías necesarias
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Cargar los datos en un DataFrame
df = pd.read_csv("Ejercicios\\graficos\\steps.csv")

#Crear el gráfico de dispersión
sns.scatterplot(x="Día", y="Pasos", data=df)

#Obliga a mostrar todos los valores en el eje x
plt.xticks(df["Día"].unique())  

#Límites del eje Y
plt.ylim(2000, 10000)

#Agregar títulos y etiquetas
plt.title("Pasos diarios de Agosto 2025")
plt.xlabel("Día")
plt.ylabel("Pasos")

#Mostrar el gráfico
plt.show()

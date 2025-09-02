import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Ejercicios\\graficos\\prices_coins.csv")

#Imprimir el nombre de las columnas del DataFrame
#print(df.columns)

sns.boxplot(x="Moneda", y="Precio", data=df)

plt.title("Distribución de Cantidades por Moneda")
plt.xlabel("Moneda")
plt.ylabel("Precio")

plt.show()
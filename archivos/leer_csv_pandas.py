import pandas as pd

# ! Llamamos la funcion usando la excepcion try / except, si no encuentra el archivo nos muestra el error.
def leer_csv_pandas():
    try:
        texto_2 = pd.read_csv("archivos\\texto_2.csv")
        print(texto_2) #Muestra el contenido de todo el archivo
        # print(archivo["Nombre"]) # * Muestra el contenido de la columna nombre
        # print(archivo["Apellido"]) # * Muestra el contenido de la columna apellido
        return texto_2
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'texto_2.csv'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

texto_3 = pd.read_csv("archivos\\texto_3.csv")

# ! De esta manera llamamos a la funcion de manera directa sin el uso de try / except, pero, para evitar un error y que el programa se cierre es mejor usar try / except.
'''
def leer_csv_pandas():
    archivo = pd.read_csv("archivos\\texto_2.csv")
    print(archivo)
    return archivo
'''

# ! __name__ nos permite saber si estamos ejecutando el archivo principal y lo igualamos a "__main__", así no necesitamos definir main en el archivo
'''
if __name__ == "__main__":
    print("Ejecutando función desde el mismo archivo:")
    leer_csv_pandas()
'''

# ! Llamada directa de la funcion
print("Llamando a la funcion con pandas")
texto_2 = leer_csv_pandas()
print("")

# ! Uso de slicing para obtener datos dentro de un array
'''array_num ="0123456789"
print(array_num[0:3])
'''

#Ordenarlo de forma ascendente
print("Ordenarlo de forma ascendente")
archivo_ordenado = texto_2.sort_values("Edad")
print(archivo_ordenado)
print("")

#Ordenarlo de forma descendente
print("Ordenarlo de forma descendente")
archivo_ordenado = texto_2.sort_values("Edad", ascending=False)
print(archivo_ordenado)
print("")

#Concatenar dos dataframes
print("Concatenar de forma descendente")
concatenar = pd.concat([texto_2, texto_3])
print(concatenar)
print("")

#Accediendo a la primera fila
# * Se explican dos maneras de mostrar la información:
'''
.head(n): devuelve las primeras n filas del DataFrame. Empieza a contar en 0 desde el encabezado.
.iloc[n]: sirve para seleccionar filas o columnas por posición numérica, mucho más flexible (puedes tomar un rango, saltos, posiciones específicas).

👉 En corto: .head() es para una vista rápida; .iloc es para indexar por posición con total control.
'''

#Accediendo a la primera fila con .head
print("Accediendo a la primera fila con .head")
primera_fila = texto_2.head(1)
print(primera_fila)
print("")

# Accediendo a la última fila con .tail
# * tail(0) devuelve un DataFrame vacío, por eso se usa tail(1) para obtener la última fila.
print("Accediendo a la última fila con .tail")
ultima_fila = texto_2.tail(1)
print(ultima_fila)
print("")

#Accediendo a un dato especifico con .loc "location"
print("Accediendo a un dato especifico con .loc")
dato_especifico = texto_2.loc[0, "Edad"]
print(f"El valor edad de la primera fila es: {dato_especifico}")
print("")

#Accediendo a la primera fila con .iloc "index location"
print("Accediendo a datoscon .iloc")
primera_fila_iloc = texto_2.iloc[0]
dato_esp_iloc = texto_2.iloc[0,2]
print("los valores de la primera fila son:")
print(primera_fila_iloc)
print("")
print(f"El valor edad de la primera fila es: {dato_esp_iloc}")
apellidos = texto_2.iloc[:,1]
print("Los apellidos son:")
print(apellidos)
print("")

#Accediento a lso datos usando condiciones (Fila Edad >41)
# * En este caso loc recorre las filas donde se cumpla la condicion > 30 y nos devuelve todas las columnas.
print("Accediento a los datos usando condiciones (Fila Edad >41)")
mayor_30 = texto_2.loc[texto_2["Edad"] > 41,:]
print(mayor_30)
print("")

#Conocer la cantidad de filas y comunas de un dataframe
print("Conocer la cantidad de filas y columnas de un dataframe con .shape y len()")
filas_y_columnas = texto_2.shape
print(f"La cantidad de filas y columnas son: {filas_y_columnas}")   
print("Cantidad de filas: ", len(texto_2))
print("Cantidad de columnas: ", len(texto_2.columns))
print("")

#Conocer el resumen de un dataframe
describe = texto_2.describe()
print(describe)

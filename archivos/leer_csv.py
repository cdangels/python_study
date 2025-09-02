import csv

with open ("archivos\\texto_2.csv", encoding="utf-8") as archivo_csv:
    print(csv.reader(archivo_csv)) #No muestra el contenido del archivo, sino que te indica que has creado un objeto que sirve para leer archivos CSV fila por fila.
    print()
    
    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)

# print(dir(csv)) dir nor permite ver los metodos de un modulo.
# print(help(csv)) help nos permite ver la documentación de un modulo.


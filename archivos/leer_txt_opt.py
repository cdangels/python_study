#Abrir el archivo con with open
with open("archivos\\texto_1.txt", encoding="utf-8") as archivo_txt:
    #Asignamos una variable a la lectura y la imprimimos
    #contenido = archivo_txt.read()
    #print(contenido)
    
    #Leemos el archivo directamente
    print(archivo_txt.read())
    
#Con with open el archivo se abre y se cierra, no es necesario cerrarlo con close
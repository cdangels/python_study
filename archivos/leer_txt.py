#Abrir un archivo con la codificación universal utf-8
archivo_txt = open("archivos\\texto_1.txt", encoding="utf-8")

'''Leer archivo completo'''
#archivo = archivo_txt.read()
#print(archivo)

'''Leer linea por linea'''
#lineas = archivo_txt.readlines()
#print(lineas)

'''Leer 1ª linea'''
linea_1 = archivo_txt.readline() #El numero dentro de los parentesis es la cantidad de caracteres a leer
print(linea_1.strip())

'''Leer 2ª linea'''
linea_2 = archivo_txt.readline()
print(linea_2)

'''.strip() - .rstrip() - -lstrip()'''
    #Estos metodos sirven para quitar espacios en blanco y saltos de línea.
    #strip() si quieres limpiar completamente los bordes.
    #rstrip() quita saltos de línea \n pero mantiene la indentación o espacios a la derecha.
    #lstrip() quita saltos de línea \n pero mantiene la indentación o espacios a la izquieda.

#Para poder recargar el archivo es encesario cerrarlo

archivo_txt.close

with open ("archivos\\texto_1.txt", 'w', encoding="utf-8") as archivo_txt: #w es write
    
    #Sobreescribiendo en el archivo, todo su contenido se borra y se reescribe con nueva información.
    #archivo_txt.write("\nPrimera línea\nSegunda línea")
    
    archivo_txt.writelines(["Primera línea","\nSegunda línea"]) 
        #Para escribir varias lineas necesitamos crear una lista [lista...]
        #El valor \n es un salto de linea, se puede poner al final de la primera linea o al principio de la segunda
    
#Con la caracteristica 'w' si no existe el archivo lo crea.
#La diferencia entre write y writelines es que write escribe una sola linea y writelines escribe varias dentro de una lista
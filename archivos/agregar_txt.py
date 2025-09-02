with open ("archivos\\texto_1.txt", 'a', encoding="utf-8") as archivo_txt: #a es append
    archivo_txt.write("\nLínea agregada con 'a' append")
    
    #cada vez que usamos append se agrega la información al final del archivo
    
    #agregar lineas con for
    
    for i in range(5):
        archivo_txt.write(f"\nLinea {i+1} agregada con for.")
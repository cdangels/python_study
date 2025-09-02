#Llamar este modulo desde una carpeta diferente

from datetime import date

def fecha_hoy():
    hoy = date.today()
    return hoy.strftime("Hoy es %d de %B de %Y")

'''print(fecha_hoy())''' #Si se agrega de esta manera se imprime lo que retorna la función.

#Formas de crear y retornar un modulo
'''
def fecha():
    print("Hoy es 10 de marzo de 2023")
    return() # Llama a la función
'''

'''
def fecha():
    return "Hoy es 10 de marzo de 2023"

print(fecha())  # Imprime lo que retorna la función
'''


'''Formas de llamar una función'''

#1. Con un argumento definido
def nombre (name):
    nombre = "Cris"
    return nombre

print (nombre("Cualquier valor, ya que no se usa el argumento sino la variable"))

#2. Sin un argumento definido

def apellido ():
    apellido = "Angel"
    return apellido

print (apellido())

#3. Darle un valor por defecto al parámetro
#Esto convierte el parámetro en opcional:

def ciudad(name=""):
    return "Bogotá"

print(ciudad())  # Esto ya no da error

#4. Devuelva el argumento "Cris" si no pasas nada, pero si pasas un nombre, lo usará como argumento.

def nombre(name="David"):
    return name

print(nombre())          # Imprime: David
print(nombre("Ciel"))    # Imprime: Ciel
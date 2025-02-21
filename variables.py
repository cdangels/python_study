#Las variables se declaran y se definen

nombre = "Cristian"
print(nombre)

#Las variables comunes son modificables o redefinibles
nombre = "David"
print(nombre)

apellido = "Angel"
print("Hola " + nombre + " " + apellido)

#Operadores de pertenencia
    #in
print("Cristian" in nombre)

    #not in
print("Cristian" not in nombre)
#_____________________________________________________________________________________

#Las constantes se declaran con mayusculas y no se pueden modificar
PI = 3.1416

#Diferentes formas de imprimir variables en un string
    #Covertir a string un número con str()
print("El valor de PI es " + str(PI))

    #Usando múltiples argumentos con ,
print("El valor de PI es", PI)

    #Usando f-strings y {} 
print(f"El valor de PI es {PI}")

#Usando .format()
print("El valor de PI es {}".format(PI))

#Las variables pueden ser de cualquier tipo
edad = 20
print(edad)



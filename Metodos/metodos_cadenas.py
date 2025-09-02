cadena1 = "Hola Cristian"
cadena2 = "Como estas?"

#Para mostrar los metodos de una variable se usa la función "dir()", esto nos muestra en pantalla los métodos que se pueden usar con la variable.
#print(dir(cadena1))

#Los metodos deben ir seguidos de la variable y un punto: Ejemplo: variable.metodo()
#Dentro de los parentesis se pueden ingresar argumentos que el método requiera, como por ejemplo el método count() que cuenta cuantas veces se repite una subcadena en una cadena.
#Podemos asignar el resultado de un método a una variable o imprimirlo directamente sin necesidad de asignarlo a una variable.

print()
print("Metodos de conversión: Lower, upper, capitalize, title")
lower = cadena1.lower() #Convierte la cadena en minusculas
print("Minusculas v1: ", lower) #Imprime la variable lower que contiene la cadena en minusculas
print("Minusculas v2: ", cadena1.lower()) #Devuelve la cadena en minusculas


print ("Mayusculas: ", cadena1.upper()) #Devuelve la cadena en mayusculas
print ("Primera en mayuscula: ", cadena1.capitalize()) #Devuelve la cadena con la primera letra en mayuscula
print ("Tipo titulo: ", cadena1.title(), cadena2.title()) #Devuelve la cadena con la primera letra de cada palabra en mayuscula

print()
print("Metodos de busqueda: Find, index")
#La diferencia entre find e index es que find devuelve -1 si no encuentra la subcadena en la cadena, mientras que index devuelve un error.

print("Find: ", cadena1.find("a")) #Devuelve la posición de la subcadena en la cadena
print("Find: ", cadena1.find("a", 5)) #Devuelve la posición de la subcadena en la cadena a partir de la posición 5
#Cuando no encuentra la subcadena en la cadena, devuelve -1
print("Find: ", cadena1.find("z")) #Devuelve -1

print("Index:", cadena1.index("la")) #Devuelve la posición de la subcadena en la cadena
#Cuando no encuentra la subcadena en la cadena, devuelve error

print()
print("Metodos de consulta:")
#isnumeric, isalpha, isalnum, isspace, islower, isupper, istitle

cadena3 = "24"
cadena4 = "Hola"
cadena5 = "24_Hola"
cadena6 = "#$%&"
#print("Es numérico: ", cadena3.isnumeric()) #Auqnue este valor sea un número, no es una cadena, por lo que no se puede usar el método isnumeric, se debe convertir a cadena.
print(cadena3, ": Es texto numérico: ", cadena3.isnumeric()) #Devuelve True si la cadena es numérica
print(cadena4, ": Es alfabético: ", cadena4.isalpha()) #Devuelve True si la cadena es alfabética solo de la A a la Z
print(cadena5, ": Es alfanumérico: ", cadena5.isalnum()) #Devuelve True si la cadena es numérica.
print(cadena6, ": Es ASCII: ", cadena6.isascii()) #Devuelve True si la cadena es ASCII

#El espacio y los caracteres especiales ASCII no son caracteres alfanuméricos, por lo que un texto con espacio o simbolos devuelve False en isalpha y isalnum.

print()
#Metodos de conteo, .count(), .len()
print("Metodos de conteo:")
print(".count()")
print(cadena1, "tiene la letra 'a': ", cadena1.count("a"), "veces.", ) #.count es un metodo que devuelve la cantidad de coincicencias que se repite la subcadena en la cadena, como es un metodo va despues de la variable seguido de . y se le pasa como argumento la subcadena que se quiere contar.
print("variable.__len__()")
print(cadena1, "tiene ", cadena1.__len__(), "caracteres.", ) #.len es una funcion que devuelve la cantidad de caracteres en la cadena, como se esta usando como metodo se debe agregar __ al principio y al final del metodo.
print("len(variable)")
print(cadena1, "tiene ", len(cadena1), "caracteres.", ) #.len es una funcion que devuelve la cantidad de caracteres en la cadena, como se esta usando como metodo se debe agregar __ al principio y al final del metodo.

print()
#Metodos de verificación de contenido, .startswith(), .endswith()
print("Metodos de verificación de contenido:")
print(".startswith()")
print(cadena1, "empieza con 'Hola': ", cadena1.startswith("Hola")) #.startswith() devuelve True si la cadena empieza con la subcadena que se pasa como argumento.
print(".endswith()")
print(cadena1, "termina con 'Cristian': ", cadena1.endswith("Cristian")) #.endswith() devuelve True si la cadena termina con la subcadena que se pasa como argumento.

print()
#Metodos de reemplazo, .replace()
print("Metodos de reemplazo:")
print(".replace()")
print("En la cadena ", cadena1, "se reemplaza 'Cristian' por 'David': ", cadena1.replace("Cristian", "David")) #.replace() reemplaza la subcadena que se pasa como primer argumento por la subcadena que se pasa como segundo argumento. Si no se encuentra la subcadena a reemplazar, devuelve la cadena original.

print()
#Metodos de separación, .split()
#.split() separa la cadena por el espacio y devuelve una lista con las palabras o los valores de la variable separadas. Si .split() no recibe argumentos, separa la cadena por el espacio.
print("Metodos de separación:")
print(".split()")
print("La cadena", cadena1, "se separa por el espacio: ", cadena1.split()) 
cadena1v2 = cadena1.split(" ")
print("La primera palabra de la lista es:", cadena1v2[0]) #Imprime la primera palabra de la lista


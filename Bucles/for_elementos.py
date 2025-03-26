# Un valor iterable es un valor que se puede recorrer en una lista, tuplas, diccionario, conjunto, cadena de texto, etc.

#for/in
''' El bucle for/in se utiliza para recorrer un valor iterable. 
Ejemplo:

animales = ['perro', 'gato', 'pez', 'loro']
for animal in animales:
    print(animal)

Para cada animal en la lista animales, imprime el animal. La variable animal se repite tantas veces como elementos haya en la lista. 
Todos los ejemplos creados con list[] tambien se pueden hacer con tuple(), set() y dict().''' 

#Ejemplo
print()
print("Lista de animales")
animales = ['perro', 'gato', 'pez', 'loro']
for animal in animales:
    print(animal)
    
#Ejemplo2
print()
print("Lista de numeros")
numeros = [1,2,3,4,5]
print(numeros)
for resultado in numeros:
    print(f"El doble de cada numero es: {resultado*2}")
    
'''Existen dos maneras de anidar ciclos for en python, la primera es utilizando dos ciclos for, la segunda es utilizando un ciclo for y un zip().'''

#Ejemplo anidado
'''El problema del for anidado, es su lógica. El for anidado recorre completamente la segunda lista (numeros) para cada elemento de la primera (animales), lo que hace que cada animal se combine con todos los números.'''
print()
print("Lista de animales y números anidados, for dentro de for.")
for animal in animales:
    for numero in numeros:
        print(f"El {animal} es el numero {numero}")

#zip()
'''Para emparejar cada animal con un solo número se usa zip():
zip(animales, numeros) empareja elementos de ambas listas por su posición (índice).
    -Si las listas tienen diferentes longitudes, zip solo tomará hasta el tamaño de la más corta. Si necesitas que ambas sean del mismo tamaño, puedes asegurarlo con zip_longest de itertools, pero eso ya depende de lo que necesites.'''

#Ejemplo 1 zip()
print()
print("Ejemplo 1 zip anidado")
for animal, numero in zip(animales, numeros):
    print(f"El {animal} es el numero {numero}")

#Ejemplo 2 zip()
print()
print("Ejemplo 2 zip por separado")
for animal, numero in zip(animales, numeros):
    print({animal})
    print({numero})
#De esta manera no anidamos lso valores sino que los imprimimos por separado.

#range()
'''range nos permite crear una secuencia de números, es muy útil para crear ciclos for que se repitan un número determinado de veces. range() tiene tres argumentos, el primero es el número de inicio, el segundo es el número final y el tercero es el paso. Ejemplo:'''
print()
print("Ejemplo de range como contador")
for count in range(10):
    print(count)

'''De esta manera podemos recorrer la lista item por item.'''

#Ejemplo con range no optimo
print()
print("Ejemplo de range no optimo")
for animal in range(len(animales)):
    print(animales[animal])
    
#Enumerate()
'''enumerate() es una función que nos permite recorrer una lista y obtener tanto el índice como el valor de cada elemento.'''
#Ejemplo con enumarate() para recorrer una lsita de manera optima.
print()
print("Ejemplo con enumerate")
for animal in enumerate(animales):
    print(animal)

print("Ejemplo con enumerate desempaquetado")
for animal in enumerate(animales):
    indice = animal[0]
    valor = animal[1]
    print(f"El animal en la posicion {indice} es {valor}")
    
#Else en un ciclo for
'''El else en un ciclo for se ejecuta cuando el ciclo for termina, siempre se ejecuta al final y si la lista no tiene elementos, el else igualmente se ejecuta. La unica forma que no se ejecute es si hay un break en el ciclo for.'''
print()
print("Ejemplo con else")
for animal in animales:
    print(animal)
else:
    print("Fin del ciclo for")
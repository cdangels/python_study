#Continue
'''Dentro del bucle for se puede usar el comando continue para saltar a la siguiente iteración sin ejecutar el código que sigue a la palabra clave continue.'''
'''El For recorre elementos de una lista, tupla, cadena de texto, etc. Mientras es while es un bucle "infinito" que se ejecuta mientras una condición sea verdadera.'''

frutas = ['manzana', 'pera', 'mango', 'fresa', 'piña']
for fruta in frutas:
    if fruta == 'pera': #Si la fruta es pera, se salta a la siguiente iteración
        continue
    print(fruta)
  
print()  
#Brake
'''Dentro del bucle for se puede usar el comando break para salir del bucle for completamente.'''
for fruta in frutas:
    if fruta == 'fresa': #Si la fruta es fresa, se sale del bucle
        break
    print(fruta)

print()
#El brake frena todo el bucle, si tenemos un else al final se ejecuta si el break no se activa.
for fruta in frutas:
    if fruta == 'banano': #Si la fruta es banano, no se ejecuta el break y se ejecuta el else
        break
    print(fruta)
else: print("se ejecuta else por que no se encontró la fruta")

print()
print("Iterar o recorres cadena de texto")
#La cadena de texto se itera caracter por caracter
cadena = "Cristian"
print(cadena)
for letra in cadena: 
    print(letra)
#Este for indica que por cada letra en la cadena, imprima la letra. letra puede ser cualquier variable, lo que interesa acá es saber que se itera dentro de la cadena que en este caso es Cristian.


print()
#Ciclo for en una sola línea
numeros = [1,2,3,4,5]
print(f"Los numeros son: {numeros}")

'''La manera clasica dentro de un ciclo for sería:'''
duplicados = list() #Creamos una lista vacia para guardar los números duplicados.
for num in numeros: 
    duplicados.append(num*2) #Por cada número en la lista de números, se multiplica por 2 y se agrega a la lista duplicados.
#Append funciona para agregar elementos a una lista.
print(f"Los numeros duplicados en un for clásico son: {duplicados}")


numeros_duplicados = [x*2 for x in numeros] #En este ciclo for por cada elemento en la lista numeros, se multiplica por 2 y se guarda en la variable numeros_duplicados. x puede ser cualquier variable.
print(f"Los numeros duplicados son: {numeros_duplicados}")
numeros_al_cuadradro = [x**2 for x in numeros]
print(f"Los numeros duplicados son: {numeros_al_cuadradro}")

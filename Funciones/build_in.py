'''Estos son algunas de las funciones predefinidas de Python, que son funciones que ya vienen incluidas en el lenguaje y se pueden utilizar directamente sin necesidad de importarlas.'''

#encontrando el numero mayor de una lista
numero = [25,48,12,5,7,8,9,10,11,13,14,15,16,17,18,19,20] #Tupla en corchetes()
numero_mas_alto = max(numero)
numero_mas_bajo = min(numero)
print(f"El numero_mas_alto es {numero_mas_alto}")  # Imprime el número más grande de la lista
print(f"El numero_mas_alto es {numero_mas_bajo}")  # Imprime el número más pequeño de la lista

#redondear
pi = 3.14159
numero = round(pi,2) #Primero el numero y luego el número de decimales a redondear.
print(f"numero pi con dos decimales es {numero}")  # Imprime el número redondeado a 2 decimales

#boolean
'''Siempre devuelve un valor booleano, True o False.
Devuelve false con 0, None, False, o listas, tuplas o diccionarios vacíos.
Devuelve true con numeros diferentes de 0, cadenas, listas, tuplas o diccionarios con contenido.'''
resultado_bool = bool()
print(f"bool() vacio es {resultado_bool}")

#all
'''Devuelve false si alguno de los elementos de un iterable es falso (o si el iterable esta vacio).
Devuelve True si todos los elementos de un iterable son verdaderos.
'''
valores_all = [1, "Carro", True]  # Lista con valores que son todos verdaderos
resultado_all = all(valores_all)  # Devuelve True porque todos los elementos son verdaderos
print(f"All con valores {valores_all[0]},{valores_all[1]},{valores_all[2]} es {resultado_all}")

#sum
numeros_sum = [3,6,9]
suma = sum(numeros_sum)  # Suma todos los números de la lista
print(f"La suma de los numeros {numeros_sum} es {suma}")  # Imprime la suma de los números
#El desempaquetado de variables tambien conocido como unpacking se puede hacer con listas, tuplas y diccionarios. Sirve para asignar los valores de una lista, tupla o diccionario a variables individuales.

#En este caso podemos crear variables nuevas tomando varoles de una tupla.
tupla = ("Cristian", "David", "Angel") #Las tuplas son inmutables.
lista = ["Cristian", "David", "Angel"] #Las listas son mutables.
set = {"Cristian", "David", "Angel"} #Los sets son mutables.

#Hay dos maneras de hacerlo, una es asignando cada valor de la tupla a una variable individual.
primer_nombre = tupla[0]
segundo_nopmbre = tupla[1]
primer_apellido = tupla[2]
print(primer_nombre)

#La otra manera es desempaquetar la tupla en variables individuales. El número de variables debe ser igual al número de elementos en la tupla.
dato1, dato2, dato3 = tupla
print(dato1)
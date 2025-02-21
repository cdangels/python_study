#LIST - crea una lista
#Se puede crear una lista con el metodo list() y pasarle como argumento una tupla, un set o un diccionario.
#La diferencia entre () y [] es que () es una tupla y [] es una lista.
lista = list(["Hola", "Mundo", "Python", "3.9",2025]) 
print("Lista original: ", lista)

#Recordemos que los metodos van despues de la variable, seguidos de un punto y se les pasa argumentos si es necesario.
#El formato de metodo es variable.metodo(argumento)
#Los metodos vistos serán: LED, APPEND, INSERT, EXTEND, POP, REMOVE, CLEAR, SORT, REVERSE

"""LEN"""
#Cuenta la cantidad de elementos de una lista
conteo_len = len(lista)
print("La lista tiene", conteo_len, "elementos.")

"""APPEND""" 
#Append agrega un elemento al final de la lista.
#La lista no esta siendo modificada, simplemente se crea un nuevo objeto con el nuevo elemento.
#Se puede agregar cualquier tipo de elemento a la lista.
add_append = "Append"
lista.append(add_append)
#Se puede de igual manera llamar a la lista y agregar el elemento sin crear una variable.
#lista.append("Append"), funciona tambien para Insert y Extend.
print("Lista Append: ", lista)

"""INSERT"""
#Agrega un elemento a la lista en el indice especificado
#Nos pide dos valores, el indice y el valor a agregar
add_insert = "Insert"
lista.insert(1, add_insert)
print("Lista Insert: ",lista)

"""EXTEND"""
#Agrega varios elementos al final de la lista
#Se debe pasar una lista con los elementos a agregar para que nos los agregue a la lista original
add_extend=(["Extend1", "Extend2"])
lista.extend(add_extend)
print("Lista Extend: ",lista)

"""POP"""
#Elimina un elemento de una lista, pide indice y devuelve valor
#Si no se pasa un indice, elimina el ultimo elemento de la lista
#Utilizando valores negativos, se puede eliminar elementos desde el final de la lista
del_pop = lista.pop(-1)
print("Lista Pop: ",lista)

"""REMOVE"""
#Eemueve un elemento de una lista, pide valor
#Si el valor no se encuentra en la lista, devuelve error
del_remove = lista.remove("Python")
print("Lista Remove: ",lista)

"""CLEAR - elimina todos los elementos de una lista"""
#Elimina todos los datos de la lista
#lista.clear()
#print("Lista Clear: ",lista)

"""SORT - ordena una lista de forma ascendente a descendente"""
#Este metodo no aldmite valores tipo string.
#Para ordenar lsitas con strings, se debe utilizar "AVERIGUAR"
#Si se intenta ordenar una lista con letras, devuelve error.
lista2=([5,410,False,2,432,True,18])
lista2.sort()
print("Lista 2 Sort: ",lista2)

#Para invertir el ordenamiento de los elementos de una lista utilizamos el argumento reverse=True dentro de los argumentos de sort.
lista2.sort(reverse=True)
print("Lista 2 Reverse: ",lista2)

"""REVERSE"""
#Invierte los elementos de una lista
lista.reverse()
print("Lista Reverse: ",lista)


"""Excisten otros metodos como index, count y demás que se pueden usar en lsitas"""
elem_index= lista.index("Append")
print("Append está en la posición ",elem_index, "de la lista.")

#lista.extend(["Append"])
elem_count= lista.count("Append")
print(lista)
if elem_count == 1:
    print("Append se encuentra ",elem_count, "vez en la lista.")
else:
    print("Append se encuentra ",elem_count, "veces en la lista.") 
    


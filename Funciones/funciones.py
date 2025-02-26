#Para crear una funcion utilizamos def, este nos permite crear una función que se puede llamar en cualquier parte del código.

def suma(a, b):
    return a + b  # Devuelve la suma

resultado_suma = suma(3, 5)  # Llamo la función y guardo el valor en la variable
print(resultado_suma)  # Imprime 8

def mult(a, b):
    return a * b  # Devuelve la suma

resultado_mult = mult(3, 5)  # Llamo la función y guardo el valor en la variable
print(resultado_mult)  # Imprime 8

#Los valores a y b son parámetros de la función, son los valores que se pasan a la función para que realice la operación.
#Los valores 3 y 5 son argumentos, son los valores que se pasan a los parámetros de la función.
#Una funcion puede tener varios parámetros, pero no puede tener más argumentos que parámetros. 
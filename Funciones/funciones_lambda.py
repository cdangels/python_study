'''
Lambda es una funcion anónima, es decir, no tiene un nombre definido.
Se utiliza para crear funciones pequeñas y rápidas, generalmente de una sola línea.

El orden de la función Lambda es:
1. nombre 
2. :
3. lambda
4. argumento
5. operación

    - Una función no es anónima ya que tiene un nombre, pla diferencia es que lambda CREA FUNCIONES ANÓNIMAS, que se pueden almacenar en una variable o pasar como argumento a otra función.
    - Puede tener tantos argumentos como se desee, pero solo una expresión "No se aconseja usar en operaciones complejas". 
    - No se pueden usar sentencias ni declaraciones dentro de una función lambda. 
'''

a = 3
b = 6
mult = lambda x : x*2  #Función lambda que multiplica el argumento por 2
sum = lambda x : x+2 #Función lambda que suma el argumento por 2
op1 = lambda a,b : (a+2)*b #Función lambda que suma el argumento por 2

print (mult(a))  # Función lambda con el argumento a
print (sum(a))  # Función lambda con el argumento a
print (op1(a,b))  # Función lambda con los argumentos 2 y 3
 

#FILTER
'''Utilizando filter para utilizar una función definida tomando datos de una lista y filtrando los resultados.'''

numeros = [1,2,3,5,8,12,15,18,20,25,30]

def par(num):
    if (num%2==0):  # Verifica si el número es impar
        return True

def impar(num):
    if (num%2==1):  # Verifica si el número es impar
        return True

pares = filter(par, numeros)
impares = filter(impar, numeros)

'''Este código devuelve un objeto filter, que es un iterador, por lo que se puede convertir a una lista o recorrerlo con un bucle.'''
print(list(pares))
print(list(impares))

print("")
print("utilizando lambda")
'Utilizando lambda'
def es_par_o_impar(num, tipo="par"):
    if tipo == "par":
        return num % 2 == 0
    elif tipo == "impar":
        return num % 2 == 1

pares = filter(lambda x: es_par_o_impar(x, "par"), numeros)
impares = filter(lambda x: es_par_o_impar(x, "impar"), numeros)

#La funcion lambda funciona como un bucle, va pasando por cada una de las posiciones de la lista con un true o un false, si la operacion dentro de lambda se cumple devuelve true, si no devuelve false, luego convertimos estas datos a una lista y se imprime.

print(list(pares))
print(list(impares))
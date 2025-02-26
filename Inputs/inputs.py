#Imput sirve para solicitar al usuario un valor, el cual se almacena en una variable.
#Todos los datos dentro de un input son string, asi sea un numero sera siendo un string.
#Para convertir un string a un numero se debe utilizar la funcion int() o float().
#Si usamos strings "6" y multiplicamos por 2 el resultado sera "66", si usamos int(6) y multiplicamos por 2 el resultado sera 12.

print("Ingrese su nombre: ")
nombre = input()
print("Hola", nombre)

#Concatenando el input con un string utilizando la funcion f-string
#Dentro de las llaves se coloca el nombre de la variable.
#print(f"Hola {nombre}")

#Trabajando con números
print("Ingresa un número entero: ")
num = int(input())
print("Multiplicalo por otro entero: ")
mult = int(input())
resultado = num * mult
print(f"El resultado es: {resultado}")

#Trabajando con decimales
print("Ingresa un número decimal: ")
num2 = float(input())
print("Multiplicalo por otro decimal: ")
mult2 = float(input())
resultado2 = num2 * mult2
print(f"El resultado es: {resultado2}")

#Por más que la multiplicación 4.5 x 2 sea 9 el resultado en flotanto sera 9.0	
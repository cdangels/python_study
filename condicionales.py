# Los condicionales nos permiten tomar decisiones en nuestro código. Son instrucciones que nos permiten evaluar si una o varias condiciones son verdaderas o falsas.
# El condicional IF nos permite evaluar una condición y ejecutar un bloque de código si esta se cumple.
# El condicional ELSE nos permite ejecutar un bloque de código si la condición del IF no se cumple.

'''Ejemplo 1 (if else)'''
num = 2
if isinstance(num, int):
    num2 = "entero"
else:
    num2 = "no es entero"

if num > 0:
    print(num, "es un numero", num2, "positivo")
    print("Esta linea hace parte del bloque de código del IF")
else:
    print(num, "es un numero", num2, "positivo")
    print("Esta linea hace parte del bloque de código del ELSE")

print("Esta linea esta fuera de los bloques de código del IF y ELSE")


'''Ejemplo 2 (if else)'''
password = "1234"
input_password = input("Ingrese su contraseña: ")

if password == input_password:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta") 
    print("Por favor intentelo de nuevo")

#Nuestro tercer condicional es ELIF, que nos permite evaluar múltiples condiciones. Elif es una abreviatura de Else If.

'''Ejemplo 3 (if elif else)'''
#Para convertir un string en un número entero usamos la función int()
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

'''Ejemplo 4 (if anidado elif else)'''
#Un condicional IF puede contener otro condicional IF dentro de él. A esto se le conoce como anidación de condicionales.
ingreso = int(input("Ingrese su ingreso mensual: "))
gastos = int(input("Ingrese sus gastos mensuales: "))

if ingreso > 1000:
    if gastos < 500:
        print("Tienes un buen ingreso y pocos gastos")
    else:
        print("Tienes un buen ingreso pero muchos gastos")

#para encadenar condiciones usamos elif se puede de dos maneras, la primera es usando and para separar las condiciones.
elif ingreso < 1000 and ingreso > 500:
    print("Tienes un ingreso promedio.")
#La segunda y más legante es encadenarlo con la variable dentro de los valores, las dos sirven.
# elif 500 < ingreso < 1000:

else:
    print("Tienes un ingreso bajo.")
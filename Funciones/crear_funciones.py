'''
- La funcion primero se crea, con los parámetros y contenido que se desea ejecutar. y luego se llama con el nombre de los argumentos creados en codigo. Se pueden usar los mismos parámetrostanto dentro de la funcion como en el codigo, ya que no afectan el comportamiento de la funcion.
- Las funciones se hacen para que retornen valores, si imprimios algo en la funcion no se podra ejecutar fuera de la misma, ya que no se guarda el valor en una variable, diferente al usar return que guarda el valor en una variable para usarla fuera de la funcion.
'''

print("Primer ejemplo.")


print ("Hola por favor digita tu nombre:")
name = input()
"""Esta es otra manera de definir una función con un parámetro que toma el valor de una variable ya definida.
#def func_par1(nombre=name):  # <- esto congela el valor de name en el momento de definir la función"""

def func_par1(nombre): #Para usar una variable ya definida dentro de la funcion, nombra el parametro de la funcion "nombre" y se le asigna el valor de la variable "name" ingresada anteriormente. Dentro de la función solo se asignas los parámetros que se van a usar dentro de la misma, en este caso solo el nombre.

    print(f"Hola {nombre}, espero que estes bien. Cuantos años tienes y en que ciudad vives?")  # Imprime un saludo personalizado
    print("Por favor ingresa tu edad:")  # Solicita al usuario que ingrese su edad
    edad_f = int(input())
    print("Por favor ingresa tu ciudad:")  # Solicita al usuario que ingrese su ciudad
    ciudad_f = input()
    return edad_f, ciudad_f  # return devuelve el valor de la variable edad, que es el número de años ingresado por el usuario, esta variable no se asigna como parametro dentro de la funcion ya que se va a usar fuera de la misma.

edad, ciudad = func_par1(name) #Llama a la función con el argumento "name" y asigna los valores retornados a las variables edad y ciudad
print(f"{name} tienes {edad} años y vives en {ciudad}.")# Imprime un saludo personalizado
print(" ")


print("Segundo ejemplo.")

#Función con varios parámetros
def func_par2(num1,num2,op):  # Función que toma dos números y una operación
    if op == "+":
        return num1 + num2  # Devuelve la suma de los dos números
    elif op == "-":
        return num1 - num2  # Devuelve la resta de los dos números
    elif op == "*":
        return num1 * num2  # Devuelve la multiplicación de los dos números
    elif op == "/":
        return num1 / num2  # Devuelve la división de los dos números
    else:
        return "Operación no válida"  # Mensaje de error si la operación no es válida
    
#Solicita al usuario que ingrese dos números y una operación
print("Por favor ingresa el primer número: ")
num1 = float(input())
print("Por favor ingresa el segundo número: ")
num2 = float(input())
print("Por favor ingresa la operación (+, -, *, /): ")
op = input()
print(f"El resultado de la operación es: {func_par2(num1, num2, op)}")  # Llama a la función con los argumentos ingresados y muestra el resultado
print(" ")


print("Tercer ejemplo.")
# Función Dalto
#crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    

print("Regalame tu nombre y tu sexo , por favor.")
nombre = input("Nombre: ")
sexo = input("Sexo (hombre, mujer, no binario, etc):" )
saludar(nombre, sexo)

saludar("Dalto","hombre")
saludar("Fran","no binario")

#Las funcione spueden tener datos predefinidos y se pueden cambiar posteriormente, por ejemplo:
def frase(nombre, apellido, adjetivo = "Inteligente"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Cristian","Angel",adjetivo="Paciente")
print(frase_resultante)


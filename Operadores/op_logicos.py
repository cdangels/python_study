#Los operadores lógicos nos permiten combinar o modificar condiciones en nuestros condicionales. Los operadores lógicos son: and, or y not.

'''AND'''
#El operador AND evalúa si dos condiciones son verdaderas. Si ambas condiciones son verdaderas, el resultado será verdadero. Si una o ambas condiciones son falsas, el resultado será falso.

#Ejemplo AND: El programa evalúa si el número ingresado por el usuario es mayor a 0 y menor a 10.
print("Ejemlo de operador AND")
print("Por favor ingrese un número mayor a 0 y que este entre 5 y 10")
num = int(input("Ingrese un número: "))
if num > 0 and 5 < num < 10:
    print(num, "es mayor a 0 y ademá está entre 5 y 10")
else:
    print(num, "no cumple las condiciones.")
print()

'''OR'''
#El operador OR evalúa si al menos una de las condiciones es verdadera. Si una o ambas condiciones son verdaderas, el resultado será verdadero. Si ambas condiciones son falsas, el resultado será falso.
#Ejemplo OR: el programa evalúa si el número ingresado por el usuario es menor a 0 o mayor a 10.
print("Ejemlo de operador OR")
print("Por favor ingrese un número entero entre a 0 y 5 o entre 10 y 15")
num2 = int(input("Ingrese un número: "))
if 0 < num2 < 5 or 10 < num2 < 15:
    print(num2, "está entre a 0 y 5 o entre 10 y 15")
else:
    print(num2, "no cumple las condiciones")
print()
 
'''NOT'''
#El operador NOT niega el resultado de una condición. Si la condición es verdadera, el resultado será falso. Si la condición es falsa, el resultado será verdadero.
#EJEMPLO NOT: el programa evalúa si el número ingresado por el usuario no es igual a 0.
print("Ejemlo de operador NOT")
print("2 es igual a 2")
num3 = 2 == 2 
print(not num3, ": La afirmación es verdadera pero devuelve falso.")
print("2 es mayor a 9")
num4 = 2 > 9 #Es falso pero devuelve verdadero
print(not num4, ": La afirmación es falsa pero devuelve verdadero.")

#AND y & son lo mismo, OR y | son lo mismo, NOT y ! son lo mismo, pero:
#AND es un operador lógico que evalúa expresiones booleanas & es un operador bit a bit (bitwise).
#OR es un operador lógico que evalúa expresiones booleanas | es un operador bit a bit (bitwise OR).

print()
#AND
Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

#OR
Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT
Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

print("Resultados operador AND")
print("True & True", Resultado)
print("False & True", Resultado2)
print("True & False", Resultado3)
print("", Resultado4)
print()
print("Resultados operador OR")
print("True | True", Resultado5)
print("False | True", Resultado6)
print("True | False", Resultado7)
print("False | False", Resultado8)
print()
print("Resultados operador NOT")
print("not True", Resultado9)
print("not False", Resultado10)





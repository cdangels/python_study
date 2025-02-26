#El orden de las operaciones aritmeticas es el siguiente:
# 1. Parentesis
# 2. Exponentes
# 3. Multiplicación y división
# 4. Suma y resta
# 5. Asociatividad
# 6. Operadores unarios
# 7. Operadores de asignación
# 8. Operadores de comparación
# 9. Operadores lógicos
# 10. Operadores de identidad


# Los operadores aritmeticos son los siguientes:
# + Suma
# - Resta
# * Multiplicación
# / División
'''La división en Python siempre retorna un número flotante y no un número entero.'''
# // División baja
'''La división baja siempre retorna el numero menor de la división, Ejemplo 11//3=3'''
#Decimales
'''Para quitar decimales de un flotante se puede usar la función round() o la función int() para convertirlo a entero.
#Ejemplo:
# print("División 11/3:", round(11/3, 3))'''

# % Módulo o resto
'''El módulo es el residuo de la división entre dos números. Ejemplo: 5/2= 2.5, el módulo es 1. Porque 2*2=4 y 5-4=1'''
# ** Potencia

a = 5
b = 2

suma= a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División baja:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)

print()
print("División normal 11/3:", round(11/3, 3))
print("División baja: 11//3", 11//3)
print("División round(11/3, 3):", round(11/3, 3))
print("División int(11/3):", int(11/3))

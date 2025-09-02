def suma (af,bf):
    return af + bf

# Solicita al usuario que ingrese dos números
a = float(input("Por favor ingresa el primer número: "))
b = float(input("Por favor ingresa el primer número: "))

resultado1 = suma(a,b)
print(f"La suma de {a} + {b} es: {resultado1}")
print(" ")

#Utilizando el operador * como argumento (*args)
#* funciona como un array, es decir, permite pasar un número variable de argumentos a la función. 
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado2 = suma("Cris",5,3,9,10,20,3)
print(resultado2)
print(" ")

#forma no optima de suma valores
def suma_total(*numeros):
    return sum(*numeros)

resultado3 = suma_total([5,3,9,10,20,3])
print(f"La suma de tus numeros es: {resultado3}")

#la fun
#Serie fibonacci

'''def fibonacci (num): 
    f0=1
    for i in range (num): 
        fq=f0+i
        if 1+i: return False 
    return True

num=(int(input("Ingresa el número a evaluar:")))
resultado = fibonacci(num)
print(f"El número {num} es fibonacci: {resultado}")'''


def fibonacci (num):
    a, b = 0,1
    fibonacci_lista = [0]
    for i in range (num): #Inicia un bucle que se ejecutará num veces (desde 0 hasta num-1).
        if b > num: return fibonacci_lista #Verifica si b es mayor que el número dado num. Si es así, termina la función y devuelve la lista actual.
        else: #Si la condición es falsa y b no es mayor que num se ejecuta el bloque siguiente.
            fibonacci_lista.append(b) #Agrega el valor actual de b a la lista
            a, b = b, a+b #Actualiza las variables: a toma el valor de b, y b toma el valor de a+b (el siguiente número de Fibonacci). Esta es una asignación simultánea que calcula el siguiente par de números en la secuencia.

#Había un pequeño error lógico. La condición if a+b > num debe ser if b > num para verificar si el número actual de Fibonacci excede el límite, no la suma de los dos siguientes números.

'''La función utiliza dos variables (a, b) para mantener los dos últimos números de la secuencia, y en cada iteración, calcula el siguiente número sumando a + b. Si esta suma excede el número límite dado, la función retorna la lista
generada hasta ese momento. De lo contrario, agrega el valor actual de 'b' a la lista y actualiza las variables
para continuar con el siguiente número de la secuencia.'''

num=(int(input("Ingresa el número a evaluar:")))
resultado = fibonacci(num)
print(f"Los numeros fibonacci hasta {num} son: {resultado}")
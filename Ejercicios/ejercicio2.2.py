#Creando una funcion que nos diga si un numero es primo o no

def es_primo (num): #Funcion: es_primo. Argumento: num.
    for i in range (2, num-1): 
        #Para cada i en el rango desde 2 a num-1. Arranca desde 2 y cada numero le resta 1. La primera opracion seria 2-1=1, la segunda 3-1=2, la tercera 4-1=3, etc. 
        if num%i==0: return False 
        #num se divide por i, si el resto de la division es 0, entonces num no es primo. 4/4=0, 3/3=0, 4/2=2, etc. 
    return True
#Crear una funcion que retorne una lista de primos
def primos_hasta (num):
    #Creamos la lista
    primos = []
    for i in range(2,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #Si lo es lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos #Devolvemos la lista

num=(int(input("Ingresa el número a evaluar:")))
resultado = es_primo(num)
print(f"El número {num} es primo: {resultado}")
print(f"Los primos hasta {num} son: {primos_hasta(num)}")
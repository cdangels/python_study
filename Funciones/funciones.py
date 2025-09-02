
# ! FUNCIONES 
'''
- Son bloques de código reutilizables. 
- Algunas son funciones predefinidas, como print(), input(), len(); matemáticas como abs(), round(), etc. 
- Otras funciones las podemos crear nosotros mismos. '''

# ! def: 
# Para crear una funcion utilizamos def, este nos permite crear una función que se puede llamar en cualquier parte del código.

'''
- Recibe argumentos y devuelve un valores.
- Se definen con def, seguida del nombre de la función y paréntesis.
- Nos permite separar el código en bloques lógicos, lo que facilita la lectura y el mantenimiento del código.
- Se pueden modificar, probar y depurar de forma independiente.'''

# ! EJEMPLOS

def funcion1(parametro): #Funsion1 es el nombre de la función, el parámetro (así llamado) es un valor que se le pasa a la función para que realice una operación.
    # Dentro se define la lógica de la función, por ejemplo:
    if parametro == "frecuencia":
        return [1, 2, 3, 4, 5]  # Ejemplo de lista de frecuencias.
    else:
        return []

numeros = funcion1("frecuencia")
#La función1 reconoce la "frecuencia" como el argumento.
#Conseguir el numero de las frecuencias en el grupo de freceuncias dentro del argumento.

def suma(a, b): #Se pueden usar muchos parámetros y se separan por comas.
    return a + b  #Devuelve la operación de los parámetros a y b.

resultado_suma = suma(3, 5)  # Llamo la función y guardo el valor en la variable
print(resultado_suma)  # Imprime 8

def mult(a, b):
    return a * b  # Devuelve la suma

resultado_mult = mult(3, 5)  # Llamo la función y guardo el valor en la variable
print(resultado_mult)  # Imprime 8

#Los valores a y b son parámetros de la función, son los valores que se pasan a la función para que realice la operación.
#Los valores 3 y 5 son argumentos, son los valores que se pasan a los parámetros de la función.
#Una funcion puede tener varios parámetros, pero no puede tener más argumentos que parámetros. 

# ! Formas de llamar y utilizar una función.
# ! ===== PARTE 1: FUNCIONES NO SIEMPRE DEBEN RETORNAR ALGO =====

# * Función que NO retorna nada (solo ejecuta acciones)
def imprimir_saludo(nombre):
    print(f"Hola, {nombre}!")
    print("¿Cómo estás?")
    # No hay return - implícitamente retorna None

# * Función que SÍ retorna algo
def calcular_suma(a, b):
    resultado = a + b
    return resultado

# Función que puede o no retornar dependiendo de la lógica
def dividir_seguro(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir entre cero")
        # No return aquí - retorna None implícitamente

# ! ===== PARTE 2: DECLARAR Y RETORNAR EN LA MISMA LÍNEA =====

# * Función simple en una línea (sin paréntesis adicionales)
def multiplicar(x, y): return x * y

# Función lambda (función anónima en una línea)
elevar_cuadrado = lambda x: x ** 2

# Función con lógica condicional en una línea
def es_par(num): return "Par" if num % 2 == 0 else "Impar"

# ===== EJEMPLOS DE USO =====
print("=== Ejemplos de uso ===")

# Función sin return
imprimir_saludo("María")
resultado1 = imprimir_saludo("Juan")  # resultado1 será None
print(f"Resultado de función sin return: {resultado1}")

print("\n" + "="*40)

# Función con return
suma = calcular_suma(5, 3)
print(f"Suma: {suma}")

print("\n" + "="*40)

# Función con return condicional
division1 = dividir_seguro(10, 2)
division2 = dividir_seguro(10, 0)
print(f"División 1: {division1}")
print(f"División 2: {division2}")

print("\n" + "="*40)

#Funciones en una línea
print(f"Multiplicación: {multiplicar(4, 5)}")
print(f"Cuadrado: {elevar_cuadrado(6)}")
print(f"¿Es par 7?: {es_par(7)}")
print(f"¿Es par 8?: {es_par(8)}")

# ===== TU FUNCIÓN ORIGINAL MEJORADA =====
print("\n" + "="*50)
print("Tu función CSV:")

# Versión que solo imprime (no retorna)
def leer_csv_solo_imprimir():
    try:
        archivo = pd.read_csv("texto_2.csv")
        print(archivo)
    except FileNotFoundError:
        print("Error: Archivo no encontrado")

# Versión que retorna datos para usar después
def leer_csv_con_return():
    try:
        archivo = pd.read_csv("texto_2.csv")
        print("Archivo cargado exitosamente")
        return archivo
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
        return None

# Versión en una línea (lambda con manejo básico)
leer_csv_simple = lambda archivo: pd.read_csv(archivo)

print("\nEjemplos:")
print("1. Función que solo imprime:")
leer_csv_solo_imprimir()

print("\n2. Función que retorna datos:")
datos = leer_csv_con_return()
if datos is not None:
    print(f"Datos obtenidos, forma: {datos.shape}")
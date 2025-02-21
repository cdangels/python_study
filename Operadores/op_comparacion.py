# Los operadores de comparación son los siguientes:
# Los operadores de comparación devuelven un valor booleano (True o False).
# == Igual a     5 == 5 # True
# != Diferente a 5 != 5 # False
# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que

a = 5
b = 2

igual = a == b
diferente = a != b
mayor = a > b
menor = a < b
mayor_igual = a >= b
menor_igual = a <= b
in_identidad = a in b
not_in = a not in b

print("Igual a:", igual)
print("Diferente a:", diferente)
print("Mayor que:", mayor)
print("Menor que:", menor)
print("Mayor o igual que:", mayor_igual)
print("Menor o igual que:", menor_igual)
print("Identidad:", in_identidad)
print("No está en:", not_in)
#Los conjuntos o sets son colecciones desordenadas de elementos únicos. Se pueden usar para realizar operaciones matemáticas como la unión, intersección, diferencia y diferencia simétrica.

#Set necesita valores iterables, por lo que no se puede pasar un valor único a un conjunto. En su lugar, se debe pasar una lista o una tupla.

conjunto1 = set([1, 2, 3, 4, 5])
print(conjunto1)

#Para crear un conjunto hasheable se debe usar la función frozenset, esta función crea un conjunto inmutable.
conjunto2 = frozenset([1, 2, 3, 4, 5])
print(conjunto2)

#No se pueden agregar conjuntos dentro de conjuntos, para poder hacerlo se debe convertir el conjunto en una lista o tupla.
conjunto2 = set([conjunto2, (6, 7, 8)]) #Se agrega el conjunto2 y una tupla.
print(conjunto2)

#Teoría de conjuntos
'''Un conjunto1 A, B, C es un subconjunto del conjunto2 A, B, C, D que a su vez es un subconjunto de un superconjunto A, B, C, D, E '''
'''Para poder determinar si un conjunto ahce parte de otro se usa el método issubset(). issubset() significa es subconjunto de (). '''

conj1={1,2,3}
conj2={1,2,3,4,5}
conj3={1,2,3,4,5,6,7}

#SUBSET
print("SUBSET")
subset1 = conj1.issubset(conj2) #True
subset2 = conj2.issubset(conj1) #False
print(f"El conjunto 1,2,3 hace parte del conjunto 1,2,3,4,5 {subset1}")
print(f"El conjunto 1,2,3,4,5 hace parte del conjunto 1,2,3 {subset2}")

#Otra manera de verificar un subconjunto es usando el comparador <=.
subset1 = conj1 <= conj2 #True
subset2 = conj2 <= conj1 #False

subset3 = conj2.issubset(conj3) #True
print(f"El conjunto 1,2,3,4,5 hace parte del conjunto 1,2,3,4,5,6,7 {subset3}")

#SUPERSET
print("SUPERSET")
'''Para determinar si un conjunto es superconjunto de otro se usa el método issuperset(). issuperset() significa es superconjunto de (). '''
superset1 = conj1.issuperset(conj2) #False
superset2 = conj2.issuperset(conj1) #True
print(f"El conjunto 1,2,3 es superconjunto del conjunto 1,2,3,4,5 {superset1}")
print(f"El conjunto 1,2,3,4,5 es superconjunto del conjunto 1,2,3 {superset2}")

#Otra manera de verificar un superconjunto es usando el comparador >=
superset1 = conj1 >= conj2 #False
superset2 = conj2 >= conj1 #True

#ISDISJOINT
print("ISDISJOINT")
'''Para determinar si dos conjuntos son disjuntos se usa el método isdisjoint(). Un conjunto es disjunto de otro si no tienen elementos en común. Si solo un elemento está en ambos conjuntos, no son disjuntos. ''' 
disjoint1 = conj1.isdisjoint(conj2) #False
print(f"El conjunto 1,2,3 y 1,2,3,4,5 son disjuntos {disjoint1}")
#Es falso porque 1,2,3 si está en 1,2,3,4,5
conj4={8,9,10}  #Conjunto disjunto
disjoint2 = conj1.isdisjoint(conj4) #True
print(f"El conjunto 1,2,3 y 8,9,10 son disjuntos {disjoint2}")

#SUBSET Manual
print("SUBSET Manual usando una función.")
def issubset_manual(conj1, conj2):
    for elem in conj1:  # Recorre cada elemento de conj1
        if elem not in conj2:  # Verifica si está en conj2
            return False  # Si uno no está, conj1 NO es subconjunto de conj2
    return True  # Si todos los valores de conj1 están en conj2 es un subconjunto de conj2
print(f"El conjunto 1,2,3 hacer parte del conjunto 1,2,3,4,5: {issubset_manual(conj1, conj2)}")  # True
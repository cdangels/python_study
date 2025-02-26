#Al crear un a tupla con tuple() se convierte una lista en una tupla inmutable.
'''Esto se hace para:
- Convertir dinámicamente una lista en tupla cuando se necesita inmutabilidad.
- Recibir datos de una función que devuelve una lista y convertirlos en una tupla para asegurarse de que no se modifiquen accidentalmente.
- Optimizar memoria y velocidad, ya que las tuplas ocupan menos espacio y son más rápidas que las listas en algunas operaciones.'''

#Se crean tuplas en:
'''Datos fijos y de solo lectura.
Datos que no deben cambiar.'''

tupla = tuple(["a", "b", "c", True, 4, 5.5])

#Otra manera de crear una tupla es sin parentesis pero separando los valores por comas.
tupla2 = "a", "b", "c", True, 4, 5.5

#Si queremos una tupla con un solo valor al final debemos poner una coma.
tupla3 = "a",
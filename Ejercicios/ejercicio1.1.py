print("EjercicioA")
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

diferencia_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_max = round(100 - (dalto_curso / otros_cursos_max * 100),1)
diferencia_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

print(f"El curso de dalto dura:")

print(f" - un {diferencia_min}% menos que el más rapido.")
print(f" - un {diferencia_max}% menos que el más lento.")
print(f" - un {diferencia_promedio}% menos que el promedio.")

#Para quitar decimales de un flotante se puede usar la función round() o la función int() para convertirlo a entero.
#Ejemplo:
# print("División 11/3:", round(11/3, 3))

print()
print("EjercicioB")
#Videos sin editas o crudos
crudos_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_prom = round(100 - (otros_cursos_promedio / crudos_promedio * 100),1)
print(f"Un curso promedio elimína {tiempo_vacio_prom}% del total.")

tiempo_vacio_dalto = round(100 - (dalto_curso / crudo_dalto * 100),1)
print(f"El curso de dalto eliminó {tiempo_vacio_dalto}% del total.")

print()
print("EjercicioC")
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio/dalto_curso*10,1)} horas de otros cursos promedio.")
frase = input("Escribeme una frase y te calculo cuanto tardarías en leerla: ")
palabras_separadas = frase.split(" ") #split() separa una cadena de texto en una lista de palabras, utilizando el espacio como separador. Se puede usar cualquier otro separador, como una coma o un punto y coma.
cantidad_de_palabras = len(palabras_separadas) #len() devuelve la cantidad de elementos de una lista, en este caso, la cantidad de palabras en la frase.
print(f"La frase tiene {cantidad_de_palabras} palabras. Si en promedio decimos 2 palabras por segundo entonces tardarías {cantidad_de_palabras/2} segundos en leerla.")
print(f"Una persona que hable 30% más rapido diría {cantidad_de_palabras} palabras en {round((cantidad_de_palabras/2)-(cantidad_de_palabras*0.3),1)} segundos.")

if cantidad_de_palabras > 100:
    print("La frase es larga y durarás más de un minuto en decirla.")
else:
    print("La frase es corta y durarás menos de un minuto en decirla.")
    
'''El viento silbaba entre las ruinas del antiguo templo, donde las llamas de las antorchas titilaban como almas atrapadas en la penumbra. Kaelor, el guerrero marcado por la guerra y la soledad, avanzaba con paso firme, sintiendo el peso invisible de una presencia que no debería estar allí. No era un enemigo. No era un aliado. Era él mismo, o algo que se le parecía demasiado. Aquel reflejo torcido, de ojos incendiados y sonrisa altiva, emergía de las sombras como si siempre hubiese estado allí, esperando. “No puedes huir de lo que eres”, susurró la figura, con su misma voz, pero más profunda, más cruel. Kaelor apretó los puños. La batalla más difícil no sería contra un ejército ni contra un monstruo… sino contra sí mismo.'''
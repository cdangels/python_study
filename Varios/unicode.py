'''Explorar caracteres Unicode desde Python'''

for i in range(0x2600, 0x260A):  # Rango de símbolos meteorológicos y misceláneos
    print(f"U+{i:04X}: {chr(i)}") # Imprimir el código Unicode y el caracter, el :04X es para formatear el código Unicode con cuatro caracteres hexadecimales

print()
import tkinter as tk
from tkinter import font

'''El prefijo \\uf generalmente indica caracteres de fuentes especiales como FontAwesome, Material Icons, etc. Para ver los disponibles en una fuente:'''
root = tk.Tk()
fa_font = font.Font(family="Font Awesome", size=12)
print(fa_font.actual())  # Ver información de la fuente

print()
'''Diferencia entre los unicode 0x \\u \\U'''
    # Python puede intentar interpretar \u \U como caracteres Unicode y fallar.
    # Solución: Escapar las barras invertidas con doble \\
        
# 0x	Número hexadecimal en Python	chr(0x1F311) → 🌑
print(chr(0x263E))  # ☾ (Luna menguante)
print(chr(0x1F311)) # 🌑 (Luna nueva)
    # \u	Unicode en cadena (máx. 4 dígitos)	"\u263E" → ☾
print("\u263E")  # ☾
    # \U	Unicode en cadena (más de 4 dígitos)	"\U0001F311" → 🌑
print("\U0001F311")  # 🌑


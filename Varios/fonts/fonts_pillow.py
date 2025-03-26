'''
Este código muestra cómo usar fuentes personalizadas en Tkinter sin necesidad de instalarlas en el sistema.
Utiliza la biblioteca PIL (Python Imaging Library, también conocida como Pillow) para renderizar texto
con una fuente personalizada en una imagen, y luego muestra esa imagen en la interfaz de Tkinter.

PIL es una potente biblioteca para procesamiento de imágenes en Python que permite:
- Crear y manipular imágenes
- Cargar y usar fuentes personalizadas (TTF, OTF)
- Dibujar texto y formas en imágenes
- Aplicar filtros y transformaciones
- Guardar imágenes en diversos formatos

Este enfoque es ideal para distribuir aplicaciones que usan fuentes personalizadas sin requerir
que el usuario final instale dichas fuentes en su sistema.
'''

import tkinter as tk  # Biblioteca estándar para interfaces gráficas
from PIL import Image, ImageDraw, ImageFont, ImageTk  # Biblioteca para manipulación de imágenes
import os  # Para operaciones con rutas de archivos
import sys  # Para acceder a variables del sistema

def resource_path(relative_path):
    """
    Obtiene la ruta absoluta al recurso, funciona tanto en desarrollo como en aplicaciones empaquetadas.
    
    Cuando una aplicación se empaqueta con PyInstaller, los archivos se extraen a una carpeta temporal.
    Esta función ayuda a encontrar la ruta correcta independientemente de cómo se ejecute la aplicación.
    
    Args:
        relative_path (str): Ruta relativa al archivo o recurso
        
    Returns:
        str: Ruta absoluta al recurso
    """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Si no estamos en un entorno empaquetado, usamos el directorio actual
        base_path = os.path.abspath(".")
    
    # Combinamos la ruta base con la ruta relativa para obtener la ruta absoluta
    return os.path.join(base_path, relative_path)

# Creamos la ventana principal de Tkinter
root = tk.Tk()
root.title("Fuente personalizada")  # Establecemos el título de la ventana
root.geometry("400x300")  # Establecemos el tamaño inicial de la ventana
root.configure(bg="#f0f0f0")  # Establecemos el color de fondo

# Definimos la ruta a la fuente personalizada
# Usamos resource_path para que funcione tanto en desarrollo como en aplicaciones empaquetadas
FONT_PATH = resource_path("Varios/fonts/BoostPlayer.otf")

# Verificamos si el archivo de la fuente existe en la ruta especificada
if not os.path.exists(FONT_PATH):
    # Si la fuente no existe, mostramos un mensaje de error
    print(f"⚠ La fuente no se encontró en: {FONT_PATH}")
    
    # Creamos una etiqueta en la ventana para mostrar el error al usuario
    error_label = tk.Label(
        root,  # Padre de la etiqueta (ventana principal)
        text=f"Error: No se encontró la fuente\n{FONT_PATH}",  # Mensaje de error
        fg="red",  # Color del texto (rojo para errores)
        bg="#f0f0f0",  # Color de fondo (igual al de la ventana)
        font=("Arial", 12)  # Fuente del sistema para el mensaje de error
    )
    error_label.pack(pady=20)  # Agregamos la etiqueta a la ventana con padding vertical
else:
    # Si la fuente existe, procedemos a usarla
    print(f"✅ Fuente encontrada en: {FONT_PATH}")
    
    try:
        # Texto que queremos mostrar con la fuente personalizada
        texto = "Hola, BoostPlayer!"
        
        # Tamaño de la fuente personalizada
        font_size = 30
        
        # Definimos las dimensiones de la imagen donde dibujaremos el texto
        img_width = 400
        img_height = 100
        
        # Creamos una nueva imagen con fondo transparente
        # RGBA: R=Red, G=Green, B=Blue, A=Alpha (transparencia)
        # El color (240, 240, 240, 0) es un gris claro totalmente transparente
        img = Image.new('RGBA', (img_width, img_height), color=(240, 240, 240, 0))
        
        # Creamos un objeto para dibujar en la imagen
        draw = ImageDraw.Draw(img)
        
        # Cargamos la fuente personalizada desde el archivo
        # ImageFont.truetype carga fuentes TrueType y OpenType
        font = ImageFont.truetype(FONT_PATH, font_size)
        
        # Obtenemos el tamaño del texto con la fuente seleccionada
        # Nota: textsize está obsoleto en versiones nuevas de PIL,
        # por eso verificamos si existe el método
        if hasattr(draw, 'textsize'):
            text_width, text_height = draw.textsize(texto, font=font)
        else:
            # Si no existe textsize, usamos valores estimados
            # En versiones más nuevas de PIL, se usaría textbbox o textlength
            text_width, text_height = 200, 40
        
        # Calculamos la posición para centrar el texto en la imagen
        text_x = (img_width - text_width) // 2 if hasattr(draw, 'textsize') else 10
        text_y = (img_height - text_height) // 2 if hasattr(draw, 'textsize') else 10
        
        # Dibujamos el texto en la imagen
        # fill=(0, 0, 0, 255) significa color negro totalmente opaco
        draw.text((text_x, text_y), texto, font=font, fill=(0, 0, 0, 255))
        
        # Convertimos la imagen de PIL a un formato que Tkinter pueda mostrar
        photo = ImageTk.PhotoImage(img)
        
        # Creamos una etiqueta para mostrar la imagen
        label = tk.Label(root, image=photo, bg="#f0f0f0")
        
        # Guardamos una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        # Esto es crucial, sin esta línea la imagen podría no mostrarse
        label.image = photo
        
        # Agregamos la etiqueta a la ventana
        label.pack(pady=20)
        
        # Añadimos una etiqueta con texto normal para comparación
        normal_label = tk.Label(
            root, 
            text="Texto con fuente del sistema", 
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        normal_label.pack(pady=10)
        
    except Exception as e:
        # Si ocurre algún error durante el proceso, lo capturamos
        print(f"⚠ Error al procesar la fuente: {e}")
        
        # Mostramos el error en la ventana
        error_label = tk.Label(
            root, 
            text=f"Error: {str(e)}", 
            fg="red",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        error_label.pack(pady=20)

# Iniciamos el bucle principal de la aplicación
# Esto mantiene la ventana abierta y responde a eventos del usuario
root.mainloop()
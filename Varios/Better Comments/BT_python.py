# ===== BETTER COMMENTS EN PYTHON =====
# Comentario normal

# ! ALERTA - Rojo
# ? PREGUNTA - Azul  
# // TACHADO - Gris tachado
# TODO: PENDIENTE - Naranja
# * IMPORTANTE - Verde brillante
# HACK: TRUCO/SOLUCIÓN TEMPORAL - Magenta
# BUG: ERROR CONOCIDO - Rojo oscuro
# NOTE: NOTA - Gris claro
# REVIEW: REVISAR - Púrpura
# FIXME: ARREGLAR - Amarillo

def ejemplo_funcion():
    # ! Esta función necesita validación urgente
    # ? ¿Debería retornar None o lista vacía?
    # TODO: Agregar manejo de errores
    # * Esta es la lógica principal del sistema
    # // Este código ya no se usa pero lo dejo comentado
    # HACK: Solución temporal hasta la v2.0
    # BUG: Falla con números negativos
    # NOTE: Basado en el algoritmo de Smith (2019)
    # REVIEW: Verificar performance con datasets grandes
    # FIXME: Corregir el bug del índice fuera de rango
    
    return "Ejemplo"

# ===== CONFIGURACIÓN PERSONALIZADA =====
# Puedes personalizar los símbolos en settings.json de VS Code:

"""
"better-comments.tags": [
    {
        "tag": "!",
        "color": "#FF2D00",
        "strikethrough": false,
        "underline": false,
        "backgroundColor": "transparent",
        "bold": false,
        "italic": false
    },
    {
        "tag": "?",
        "color": "#3498DB",
        "strikethrough": false,
        "underline": false,
        "backgroundColor": "transparent",
        "bold": false,
        "italic": false
    },
    {
        "tag": "//",
        "color": "#474747",
        "strikethrough": true,
        "underline": false,
        "backgroundColor": "transparent",
        "bold": false,
        "italic": false
    }
]
"""
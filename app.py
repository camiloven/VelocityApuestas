import json
import datetime

# 1. Tu lógica existente para obtener los picks del día
# (Mantén aquí tu código que obtiene los partidos de la API)
# Supongamos que ya tienes la lista 'picks' lista

# 2. Guardar en picks.json (Lo de siempre)
with open('picks.json', 'w') as f:
    json.dump(picks, f)

# 3. Guardar en historial.json (Lo nuevo)
try:
    with open('historial.json', 'r') as f:
        historial = json.load(f)
except:
    historial = []

# Añadimos los picks de hoy al historial
historial.extend(picks)

# Guardamos solo los últimos 50 elementos para que el archivo no crezca demasiado
with open('historial.json', 'w') as f:
    json.dump(historial[-50:], f)

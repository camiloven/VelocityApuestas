import json
import os

# Supongamos que aquí obtienes tus 'picks' (lista de diccionarios)
# picks = [...] 

# Guardar en picks.json (Día actual)
with open('picks.json', 'w') as f:
    json.dump(picks, f)

# Guardar en historial.json (Acumulado)
historial = []
if os.path.exists('historial.json'):
    with open('historial.json', 'r') as f:
        try:
            historial = json.load(f)
        except:
            historial = []

# Añadimos los nuevos picks y mantenemos los últimos 50
historial = picks + historial
with open('historial.json', 'w') as f:
    json.dump(historial[:50], f)

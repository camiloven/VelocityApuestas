import json
import urllib.request
import datetime

API_KEY = '41c3641633091197d7e47be1c2e1d7e4'
FECHA = datetime.datetime.now().strftime('%Y-%m-%d')

# Usamos endpoints clave
endpoints = [
    f"https://v3.football.api-sports.io/fixtures?date={FECHA}",
    f"https://v1.basketball.api-sports.io/games?date={FECHA}"
]

todos_los_datos = []

for url in endpoints:
    try:
        req = urllib.request.Request(url)
        req.add_header('x-apisports-key', API_KEY)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            # Nos aseguramos de extender la lista con todos los resultados
            if 'response' in data:
                todos_los_datos.extend(data['response'])
    except Exception as e:
        print(f"Error en {url}: {e}")

# Guardamos el archivo completo
with open('picks.json', 'w') as f:
    json.dump(todos_los_datos, f)

import json
import urllib.request
import datetime

# --- CONFIGURACIÓN ---
API_KEY = '41c3641633091197d7e47be1c2e1d7e4'
FECHA = datetime.datetime.now().strftime('%Y-%m-%d')

# Lista de todas tus fuentes activas
fuentes = [
    f"https://v3.football.api-sports.io/fixtures?date={FECHA}",
    f"https://v1.basketball.api-sports.io/games?date={FECHA}",
    f"https://v1.baseball.api-sports.io/games?date={FECHA}",
    f"https://v1.hockey.api-sports.io/games?date={FECHA}",
    f"https://v1.american-football.api-sports.io/games?date={FECHA}",
    f"https://v1.rugby.api-sports.io/games?date={FECHA}",
    f"https://v1.volleyball.api-sports.io/games?date={FECHA}",
    f"https://v1.handball.api-sports.io/games?date={FECHA}"
]

def obtener_datos(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('x-apisports-key', API_KEY)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('response', [])
    except Exception as e:
        print(f"Error en {url}: {e}")
        return []

# --- PROCESAMIENTO ---
todos_los_datos = []
for url in fuentes:
    print(f"Consultando: {url}")
    datos = obtener_datos(url)
    todos_los_datos.extend(datos)

# Guardar en archivo único para tu web
with open('picks.json', 'w') as f:
    json.dump(todos_los_datos, f)

print(f"Proceso completado. Se guardaron {len(todos_los_datos)} eventos.")

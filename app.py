import json
import urllib.request
import datetime

# Tu API Key real va aquí
API_KEY = '41c3641633091197d7e47be1c2e1d7e4' 
# URL para el día de hoy
fecha = datetime.datetime.now().strftime('%Y-%m-%d')
URL = f"https://v3.football.api-sports.io/fixtures?date={fecha}"

req = urllib.request.Request(URL)
req.add_header('x-apisports-key', API_KEY)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        picks = data.get('response', [])
        
        # Guardar en picks.json
        with open('picks.json', 'w') as f:
            json.dump(picks, f)
except Exception as e:
    print(f"Error al conectar: {e}")

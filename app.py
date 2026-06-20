import json, urllib.request, datetime

API_KEY = '41c3641633091197d7e47be1c2e1d7e4'
FECHA = datetime.datetime.now().strftime('%Y-%m-%d')
urls = [f"https://v3.football.api-sports.io/fixtures?date={FECHA}", f"https://v1.basketball.api-sports.io/games?date={FECHA}"]

datos_finales = []

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'x-apisports-key': API_KEY})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if 'response' in data:
                for item in data['response']:
                    # Traducimos los datos al formato que index.html espera:
                    local = item.get('teams', {}).get('home', {}).get('name', 'Local')
                    visitante = item.get('teams', {}).get('away', {}).get('name', 'Visitante')
                    goles_h = item.get('goals', {}).get('home', 0)
                    goles_a = item.get('goals', {}).get('away', 0)
                    
                    datos_finales.append({
                        "equipo": f"{local} vs {visitante}",
                        "pronostico": f"Resultado: {goles_h} - {goles_a}"
                    })
    except Exception as e:
        print(f"Error: {e}")

with open('picks.json', 'w') as f:
    json.dump(datos_finales, f)
    

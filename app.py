import json, urllib.request, datetime

API_KEY = '41c3641633091197d7e47be1c2e1d7e4'
FECHA = datetime.datetime.now().strftime('%Y-%m-%d')
# Solicitamos hasta 80 partidos
url_fixture = f"https://v3.football.api-sports.io/fixtures?date={FECHA}"

datos_finales = []

try:
    req = urllib.request.Request(url_fixture, headers={'x-apisports-key': API_KEY})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        if 'response' in data:
            # Procesamos hasta 80 partidos
            for item in data['response'][:80]: 
                fixture_id = item['fixture']['id']
                local = item['teams']['home']['name']
                visitante = item['teams']['away']['name']
                
                url_pred = f"https://v3.football.api-sports.io/predictions?fixture={fixture_id}"
                req_p = urllib.request.Request(url_pred, headers={'x-apisports-key': API_KEY})
                try:
                    with urllib.request.urlopen(req_p) as res_p:
                        pred_data = json.loads(res_p.read().decode())
                        # Verificamos si hay predicción
                        if pred_data['response']:
                            pred = pred_data['response'][0]['predictions']['winner']['name']
                            prob = pred_data['response'][0]['predictions']['winner']['comment']
                            texto_pronostico = f"Favorito: {pred} ({prob})"
                        else:
                            texto_pronostico = "Sin predicción disponible"
                except:
                    texto_pronostico = "Error consultando predicción"
                
                datos_finales.append({
                    "equipo": f"{local} vs {visitante}",
                    "pronostico": texto_pronostico
                })
except Exception as e:
    print(f"Error general: {e}")

with open('picks.json', 'w') as f:
    json.dump(datos_finales, f)
    

import urllib.request
import json
import random

def actualizar_picks():
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4328"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            picks = []
            for e in data['events'][:5]: # Tomamos 5 partidos
                # Lógica simple de pronóstico
                pronostico = "Gana " + (e['strHomeTeam'] if random.random() > 0.5 else e['strAwayTeam'])
                picks.append({
                    "equipo": f"{e['strHomeTeam']} vs {e['strAwayTeam']}",
                    "fecha": e['dateEvent'],
                    "pronostico": pronostico
                })
            with open('picks.json', 'w') as f:
                json.dump(picks, f)
            print("5 partidos y pronósticos generados.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    actualizar_picks()

import urllib.request
import json

def actualizar_picks():
    # Buscamos eventos para el 20 de junio de 2026
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d=2026-06-20"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            if not data.get('events'):
                print("No hay partidos para esta fecha.")
                return
            
            picks = []
            for e in data['events']:
                # Aquí puedes añadir tu propia lógica de "análisis"
                # Por ahora, un mensaje fijo o una predicción basada en equipo local
                picks.append({
                    "equipo": f"{e['strHomeTeam']} vs {e['strAwayTeam']}",
                    "fecha": e['dateEvent'],
                    "pronostico": f"Análisis técnico: Favorito {e['strHomeTeam']}"
                })
            with open('picks.json', 'w') as f:
                json.dump(picks, f)
            print("Partidos del 20 de junio guardados.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    actualizar_picks()

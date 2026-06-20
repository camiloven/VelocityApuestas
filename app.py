import urllib.request
import json
import sys

def actualizar_picks(fecha):
    url = f"https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d={fecha}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            if not data.get('events'):
                print("[]") # Retorna JSON vacío si no hay partidos
                return
            
            picks = [{"equipo": f"{e['strHomeTeam']} vs {e['strAwayTeam']}", "fecha": e['dateEvent']} for e in data['events']]
            print(json.dumps(picks))
    except:
        print("[]")

if __name__ == "__main__":
    fecha = sys.argv[1] if len(sys.argv) > 1 else "2026-06-20"
    actualizar_picks(fecha)

import urllib.request
import json

def actualizar_picks():
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4328"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            picks = [{"equipo": f"{e['strHomeTeam']} vs {e['strAwayTeam']}", "fecha": e['dateEvent']} for e in data['events'][:3]]
            with open('picks.json', 'w') as f:
                json.dump(picks, f)
            print("Picks actualizados exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    actualizar_picks()

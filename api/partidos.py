from http.server import BaseHTTPRequestHandler
import urllib.request
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        fecha = params.get('fecha', ['2026-06-20'])[0]
        
        url = f"https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d={fecha}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.load(response)
                events = data.get('events', [])
                picks = [{"equipo": f"{e['strHomeTeam']} vs {e['strAwayTeam']}", "fecha": e['dateEvent']} for e in events]
        except:
            picks = []
            
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(picks).encode())
        return

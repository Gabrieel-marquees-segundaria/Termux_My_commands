import http.server
import socketserver

PORT = 8080

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Permite acesso de qualquer origem
        self.send_header("Access-Control-Allow-Origin", "*")
        # Se precisar suportar requisições com métodos além de GET/POST
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Servidor com CORS rodando em http://localhost:{PORT}")
    httpd.serve_forever()

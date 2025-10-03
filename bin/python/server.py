import http.server
import socketserver
import logging
import sys

# --- Configuração do logging ---
logger = logging.getLogger("ServidorHTTP")
logger.setLevel(logging.DEBUG)

# Handler para o terminal → WARNING e acima
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

# Handler para erros em arquivo → ERROR e acima
error_file_handler = logging.FileHandler("server_errors.log", encoding="utf-8")
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
))

# Handler para acessos em arquivo → tudo (INFO e acima)
access_file_handler = logging.FileHandler("server_access.log", encoding="utf-8")
access_file_handler.setLevel(logging.INFO)
access_file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(message)s"
))

logger.addHandler(console_handler)
logger.addHandler(error_file_handler)
logger.addHandler(access_file_handler)


# --- Handler customizado para requisições ---
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        """
        Redireciona logs de acesso (requisições HTTP)
        Exemplo de linha salva em server_access.log:
        2025-09-18 15:00:01 - 127.0.0.1 - "GET /index.html" 200
        """
        client_ip = self.client_address[0]
        message = f'{client_ip} - "{self.command} {self.path}" {self.log_date_time_string()}'
        logger.info(message)
        print(message)


# --- Servidor customizado para ignorar erros de desconexão ---
class MyTCPServer(socketserver.TCPServer):
    def handle_error(self, request, client_address):
        exctype, value, tb = sys.exc_info()
        if exctype in (ConnectionResetError, BrokenPipeError):
            return  # ignora cliente que fechou antes da hora
        logger.error("Erro com cliente %s: %s", client_address, value)


# --- Executa servidor ---
if __name__ == "__main__":
    PORT = 8080
    with MyTCPServer(("", PORT), MyHandler) as httpd:
        logger.warning(f"Servidor rodando em http://localhost:{PORT}")
        httpd.serve_forever()

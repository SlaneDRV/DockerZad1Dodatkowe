import http.server
import socketserver
import logging
import datetime
from http import HTTPStatus
import socket

PORT = 8000
AUTHOR = "Dzmitry Revutski"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        current_time = datetime.datetime.now()
        local_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        response = f"IP klienta: {client_ip}\nCzas serwera: {local_time}\n"

        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

        logging.info(f"Handled request from {client_ip} at {local_time}")


if __name__ == "__main__":
    logging.basicConfig(filename='server.log', level=logging.INFO)
    logging.info(f"Server started at {datetime.datetime.now()} by {AUTHOR} on port {PORT}")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logging.info(f"Serving on port {PORT}")
        httpd.serve_forever()

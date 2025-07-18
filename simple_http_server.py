#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        logging.info(f"Received POST request from {self.client_address}")
        logging.info(f"Headers: {self.headers}")
        logging.info(f"Body:\n{post_data.decode('utf-8')}")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"POST received\n")

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Simple HTTP Server is running.\n")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting HTTP server on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("HTTP server stopped.")

if __name__ == '__main__':
    run()

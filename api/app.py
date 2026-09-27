from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
from datetime import datetime, timezone

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "portfolio-api"
            }
            status = 200

        elif self.path == "/api/info":
            response = {
                "service": "portfolio-api",
                "hostname": socket.gethostname(),
                "status": "running",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            status = 200

        else:
            response = {"error": "not found"}
            status = 404

        body = json.dumps(response).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(
            f"{self.client_address[0]} - "
            f"{format % args}",
            flush=True
        )

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

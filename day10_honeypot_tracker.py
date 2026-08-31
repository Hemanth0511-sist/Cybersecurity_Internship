from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json


LOG_FILE = "honeypot_log.json"


class HoneyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?")
        }

        # Display captured lab visit
        print("\n[HONEYPOT EVENT]")
        print(json.dumps(entry, indent=4))

        # Save event to JSON log
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as file:
                logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = []

        logs.append(entry)

        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(logs, file, indent=4)

        # Safe response
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        message = """
        <html>
        <head>
            <title>Security Awareness Lab</title>
        </head>
        <body>
            <h1>Honeypot Awareness Lab</h1>
            <p>This is an authorized cybersecurity training environment.</p>
            <p>Your visit has been recorded for the lab demonstration.</p>
        </body>
        </html>
        """

        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format, *args):
        # Suppress default HTTP server logging
        pass


print("=" * 65)
print("          DAY 10 - HONEYPOT LINK TRACKER")
print("=" * 65)
print()
print("Authorized localhost lab only")
print("Server: http://127.0.0.1:8080")
print("Log file: honeypot_log.json")
print()
print("Open http://127.0.0.1:8080/lab-bait")
print("in your browser to generate a test event.")
print()
print("Press CTRL+C to stop the server.")
print("=" * 65)

server = HTTPServer(("127.0.0.1", 8080), HoneyHandler)
server.serve_forever()
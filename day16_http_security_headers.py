from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from urllib.error import URLError
import threading
import time


HOST = "127.0.0.1"
PORT = 8080
TEST_URL = f"http://{HOST}:{PORT}/"


class LabServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        # Security headers used by the internal training application
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'"
        )
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header(
            "Referrer-Policy",
            "strict-origin-when-cross-origin"
        )
        self.send_header(
            "Permissions-Policy",
            "geolocation=(), microphone=(), camera=()"
        )

        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Internal Security Lab</title>
        </head>
        <body>
            <h1>Internal Security Training Application</h1>
            <p>Day 16 HTTP Security Header Analysis Lab</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        return


def start_server():
    server = HTTPServer((HOST, PORT), LabServer)
    server.serve_forever()


def analyze_headers(url):
    print("\nConnecting to internal lab...")
    print(f"Target URL : {url}")

    try:
        response = urlopen(url, timeout=5)

        print(f"HTTP Status: {response.status}")

        headers = response.headers

        security_headers = {
            "Content-Security-Policy": "CSP",
            "X-Content-Type-Options": "MIME Sniffing Protection",
            "X-Frame-Options": "Clickjacking Protection",
            "Referrer-Policy": "Referrer Control",
            "Permissions-Policy": "Browser Feature Restriction"
        }

        print("\nSecurity Header Analysis")
        print("-" * 65)

        present = 0
        missing = 0

        for header, purpose in security_headers.items():
            value = headers.get(header)

            if value:
                print(f"[PASS] {header}")
                print(f"       Value  : {value}")
                print(f"       Purpose: {purpose}")
                present += 1
            else:
                print(f"[WARN] {header}")
                print("       Status : Missing")
                print(f"       Purpose: {purpose}")
                missing += 1

        print("\nSecurity Summary")
        print("-" * 65)
        print(f"Security headers checked : {len(security_headers)}")
        print(f"Headers present          : {present}")
        print(f"Headers missing          : {missing}")

        if missing == 0:
            print("Overall status           : GOOD")
        else:
            print("Overall status           : REVIEW REQUIRED")

        print("\nCSP Analysis")
        print("-" * 65)

        csp = headers.get("Content-Security-Policy")

        if csp:
            print("CSP Status               : ENABLED")
            print("Policy                   :", csp)
            print("Effect                   : Restricts script sources to")
            print("                           trusted locations defined by policy.")
        else:
            print("CSP Status               : NOT ENABLED")

    except URLError as error:
        print("\n[ERROR] Could not connect to internal lab.")
        print(f"Reason: {error}")


def main():
    print("=" * 65)
    print("       DAY 16 - HTTP SECURITY HEADER ANALYSIS")
    print("=" * 65)

    print("\nAuthorized defensive training environment.")
    print("Testing localhost only.")

    server_thread = threading.Thread(
        target=start_server,
        daemon=True
    )

    server_thread.start()

    time.sleep(1)

    analyze_headers(TEST_URL)

    print("\n" + "=" * 65)
    print("             ANALYSIS COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    main()
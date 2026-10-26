"""Server lokal untuk galaksi interaktif.

Cara pakai:
    python server.py
Browser akan terbuka otomatis di http://localhost:8000
Tekan Ctrl+C di terminal untuk berhenti.
"""
import http.server
import os
import socketserver
import threading
import webbrowser

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Selalu kirim file terbaru, jangan pakai cache browser
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # terminal tetap bersih


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Galaksi berjalan di {url}  (Ctrl+C untuk berhenti)")
    print(f"Folder yang disajikan: {os.getcwd()}")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")

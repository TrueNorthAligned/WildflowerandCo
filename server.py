#!/usr/bin/env python3
"""
Wildflower & Co. — Storefront Web Server

Serves the storefront website on port 3000 (all interfaces).
"""

import http.server
import socketserver
import os

PORT = 3000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[Storefront] {args[0]} {args[1]} {args[2]}")


if __name__ == "__main__":
    print(f"🌿 Wildflower & Co. Storefront")
    print(f"📡 Serving on http://0.0.0.0:{PORT}")
    print(f"📂 Serving files from: {DIRECTORY}")
    print(f"🔒 Press Ctrl+C to stop\n")

    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        httpd.serve_forever()
import http.server
import socketserver

# Define the port to serve on
PORT = 8000

# Set up the handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
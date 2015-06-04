import http.server
import socketserver


PORT = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/webhook'] # or wherever you store the script... cgi_bin is default without this
server_address = ("", PORT)

httpd = http.server.HTTPServer(server_address, handler)

print("serving at port", PORT)
httpd.serve_forever()


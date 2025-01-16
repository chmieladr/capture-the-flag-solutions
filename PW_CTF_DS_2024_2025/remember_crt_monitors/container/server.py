import os
import subprocess

import http.server
import socketserver

flag = os.getenv("FLAG", "")
out = open("messages", "w")
ret = subprocess.run(["./encrypt"], env={"FLAG": "PW{" + flag + "}"}, stdout=out)

out.close()


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    pass


httpd = socketserver.TCPServer(("0.0.0.0", 80), RequestHandler)
httpd.serve_forever()

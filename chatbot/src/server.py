from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

# instantiate chatbot 
import chatbot
english_chatbot = chatbot.get_english_chatbot()  # can add multi-lingual support here

# define a simple http server that will use the chatbot to respond to a user
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))
        chatbot_response = english_chatbot.get_response(body['message'])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(str(chatbot_response).encode('utf-8'))
        self.wfile.write(response.getvalue())
  

# run the server on port 8000
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

# get relevant training data
import data
training_data = data.get_training_data()

# instantiate classifier
import classifier
nltk_classifier = classifier.NLTKClassifier(data.get_training_data())

# define a simple http server that will use the chatbot to respond to a user
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))
        classification = nltk_classifier.classify(body['message'])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(classification.encode('utf-8'))
        self.wfile.write(response.getvalue())
  

# run the server on port 8000
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
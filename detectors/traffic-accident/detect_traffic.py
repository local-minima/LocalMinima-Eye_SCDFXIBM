# python3 -m pip install --upgrade tensorflow efficientnet keras pillow

from http.server import BaseHTTPRequestHandler, HTTPServer
import efficientnet.keras
import efficientnet.tfkeras
import tensorflow as tf
from PIL import Image
import numpy as np
import argparse
import os
import io


cwd = os.getcwd()

HOSTNAME = "0.0.0.0"
PORT = 8080

args = {}

def predict(path):
    img = Image.open(path)
    new_img = np.array(img.resize((224,224)))
    new_img = np.expand_dims(new_img, axis=0)

    model = tf.keras.models.load_model(cwd + "/traffic-net10.h5")
    return model.predict(new_img)

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        length = int(self.headers['content-length'])
        thisline = self.rfile.readline() + self.rfile.readline() + self.rfile.readline() + self.rfile.readline()
        length -= len(thisline)
        data = self.rfile.read(length)

        self.wfile.write(bytes(str(1 - predict(io.BytesIO(data))), 'utf8'))
        self.send_response(200)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", default="", help="Input path to image you want to predict")
    args = parser.parse_args()

    if args.image != "":
        print(1 - predict(args.image))
        os.exit(0)

    webServer = HTTPServer((HOSTNAME, PORT), Server)

    try:
        webServer.serve_forever()
        print("started")
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

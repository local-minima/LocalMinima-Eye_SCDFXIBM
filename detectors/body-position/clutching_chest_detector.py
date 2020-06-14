from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import math
import sys
import io

POSEENDPOINT = "https://scdfxibm2020.garykim.dev/pose/model/predict"

HOSTNAME = "0.0.0.0"
PORT = 8080


def apiData(path=""):
    files = {
        'file': open(path, 'rb').read()
    }
    res = requests.post(POSEENDPOINT, files=files)
    return res.json()


def get_distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def get_chest_loc(left_x, right_x, left_y, right_y):
    mid_point_x = (right_x + left_x) / 2
    mid_point_y = (right_y + left_y) / 2
    slope = (right_y - left_y) / (right_x - left_x)
    perpendicular_line = -1 / slope
    unit_vector_x = 1 / math.sqrt(1 + perpendicular_line ** 2)
    unit_vector_y = slope / math.sqrt(1 + perpendicular_line ** 2)
    length_of_line = get_distance(left_x, right_x, left_y, right_y)
    chest_loc_x = mid_point_x + (length_of_line / 10) * unit_vector_x
    chest_loc_y = mid_point_y + (length_of_line / 10) * unit_vector_y
    return chest_loc_x, chest_loc_y


def is_person_clutching_chest(person_data, threshold=40):
    body_parts = person_data['body_parts']
    if "RShoudler" not in body_parts or "LShoudler" not in body_parts:
        return False

    else:
        left_x, right_x = body_parts['LShoulder']['x'], body_parts['RShoulder']['x']
        left_y, right_y = body_parts['LShoulder']['y'], body_parts['RShoulder']['y']
        chest_loc_x, chest_loc_y = get_chest_loc(left_x, right_x, left_y, right_y)
        if "RWrist" in body_parts:
            if get_distance(body_parts['RWrist']['x'], chest_loc_x,
                            body_parts['RWrist']['y'], chest_loc_y) <= threshold:
                return True
        if "LWrist" in body_parts:
            if get_distance(body_parts['LWrist']['x'], chest_loc_x,
                            body_parts['LWrist']['y'], chest_loc_y) <= threshold:
                return True
        return False


def is_person_clutching_chest_in_image(path):
    data = apiData(path)
    for person in data['predictions']:
        if is_person_clutching_chest(person):
            return True
    return False


class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        length = int(self.headers['content-length'])
        thisline = self.rfile.readline() + self.rfile.readline() + self.rfile.readline() + self.rfile.readline()
        length -= len(thisline)
        data = self.rfile.read(length)

        self.wfile.write(bytes(str(is_person_clutching_chest_in_image(io.BytesIO(data))), 'utf8'))
        self.send_response(200)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Expecting 1 command line argument")
        sys.exit(1)
    webServer = HTTPServer((HOSTNAME, PORT), Server)

    try:
        webServer.serve_forever()
        print("started")
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
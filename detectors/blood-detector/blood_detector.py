import cv2
import requests
import os
import argparse

POSEENDPOINT = "https://scdfxibm2020.garykim.dev/pose/model/predict"

parser = argparse.ArgumentParser()
parser.add_argument("image_path", help="Input path to image you want to predict")
args = parser.parse_args()


# Get Pose Key point data
def apiData(path=""):
    files = {
        'file': open(path, 'rb').read()
    }
    res = requests.post(POSEENDPOINT, files=files)
    return res.json()


# Creates a list [(x1,y1), (x2,y2), (xn,yn)] of the the keypoints given the json data for a person
def format_key_points_person(person_data):
    key_point_list = []
    for key_point in person_data['body_parts']:
        if [float(key_point['score']) > 0.5]:
            key_point_list.append((key_point['x'], key_point['y']))
    return key_point_list


# Returns binary mask of image, where 255 = blood, 0 = no blood
def get_blood_mask(path_to_image):
    img = cv2.imread(path_to_image)
    lower_red = (0, 0, 150)
    upper_red = (90, 90, 255)
    mask = cv2.inRange(img, lower_red, upper_red)
    return mask


# Returns bounding box of person given a list of their pose key points
def get_bounding_box(key_points):
    min_x, min_y = key_points[0]
    max_x, max_y = key_points[0]
    for key_point in key_points:
        if key_point[0] < min_x:
            min_x = key_point[0]
        elif key_point[0] > max_x:
            max_x = key_point[0]
        if key_point[1] < min_y:
            min_y = key_point[1]
        elif key_point[1] > max_y:
            max_y = key_point[1]
    return [(min_x, min_y), (max_x,max_y)]


# Returns whether or not there is a significant amount of blood near a person
def blood_near_person(key_points, path_to_img, amount_threshold=1000):
    blood_mask = get_blood_mask(path_to_img)
    #cv2.imshow("mask", blood_mask)
    #cv2.waitKey()
    bounding_box = get_bounding_box(key_points)
    counter = 0
    for x_pixel in range(bounding_box[0][0], bounding_box[1][0]):
        for y_pixel in range(bounding_box[0][1], bounding_box[1][1]):
            if blood_mask[y_pixel][x_pixel] == 255:
                counter += 1
            if counter == amount_threshold:
                return True
    return False


# Checks if blood is near any person
def blood_near_any_person(path_to_img):
    data = apiData(path_to_img)

    for person in data['predictions']:
        if blood_near_person(format_key_points_person(person), path_to_img):
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

        self.wfile.write(bytes(str(blood_near_any_person(io.BytesIO(data))), 'utf8'))
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

import requests
import sys
import math

import numpy as np

POSEENDPOINT = "https://scdfxibm2020.garykim.dev/pose/model/predict"
#POSEENDPOINT = "http://httpbin.org/post"

# Top down body parts
PRIORITIES = ["REye", "LEye", "REar", "LEar", "Nose", "Neck", "RShoudler", "LShoulder", "RHip", "LHip", "RKnee", "LKnee", "LAnkle", "RAnkle"]

def isLyingDown(path=""):
    files = {
        'file':  open(path, 'rb').read()
    }
    res = requests.post(POSEENDPOINT, files=files)
    data = res.json()

    # Make prediction
    predictions = []
    for person in data['predictions']:
        x = np.array(list(map(lambda i: i['x'], person['body_parts']))).reshape((-1, 1))
        y = np.array(list(map(lambda i: i['y'], person['body_parts'])))
        top = significantPoint(True, person['body_parts'])
        bottom = significantPoint(False, person['body_parts'])
        if top['part_id'] == bottom['part_id']:
            predictions.append(0)
            continue
        diffX = top['x'] - bottom['x']
        diffY = top['y'] - bottom['y']
        if diffX == 0:
            diffX = 0.00000001
        prediction = 1 - (math.atan(abs(diffY/diffX)) / (math.pi / 2))
        predictions.append(prediction)
    return predictions

def significantPoint(top=False, body_parts = []):
    working = PRIORITIES
    if not top:
        working = list(reversed(working))
    for looking in working:
        for part in body_parts:
            if looking == part['part_name']:
                return part
    # Means that there are literally no usable points. At this point, assume they are standing up
    return {
        'part_id': 0,
        'part_name': 'fake',
        'score': "0",
        'x': 0,
        'y': 100 if top else 0
    }

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Expecting 1 command line argument")
        sys.exit(1)
    print(isLyingDown(sys.argv[1]))

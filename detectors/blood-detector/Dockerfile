FROM python:3.7

RUN python3 -m pip install --upgrade requests opencv-python pillow
WORKDIR /app
COPY . /app
CMD ["python", "blood_detector.py"]

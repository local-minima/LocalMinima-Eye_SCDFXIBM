FROM python:3.7

RUN python3 -m pip install --upgrade tensorflow efficientnet keras pillow
WORKDIR /app
COPY . /app
CMD ["python", "detect_traffic.py"]

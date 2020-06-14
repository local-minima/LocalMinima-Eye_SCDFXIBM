# IBM Cloud Usage

Our project relies very heavily on IBM Cloud services to function. In normal operation, the system will very often call several APIs to identify whether a frame includes a dangerous situation. 

This software uses the following APIs that are hosted on IBM Cloud:

* Traffic Accident Detector: `https://scdfxibm2020.garykim.dev/traffic`
* Human Pose Estimator: `https://scdfxibm2020.garykim.dev/pose/model/predict`
* Fire Detector: `https://scdfxibm2020.garykim.dev/fire`
* Abnormal Body Position Detector: `https://scdfxibm2020.garykim.dev/body`
* Chest Clenching Detector: `https://scdfxibm2020.garykim.dev/chest`
* Blood Detector: `https://scdfxibm2020.garykim.dev/blood`

We started a virtual server on IBM with the hostname `ubuntu01.ibm.garykim.dev`. On the virtual server, several OCI containers are running, each responsible for one of the API endpoints. These endpoints range between TensorFlow powered complex AI models to machine vision algorithms. Apache HTTPD is also installed to act as a reverse proxy for all these services and to add SSL/TLS, so it can be accessed over `https` to help ensure the security of any data sent to the endpoint and the authenticity of the returned data.

# LocalMinima-Funnel_SCDFXIBM

![Screenshot](docs/screenshot.png)
*Since we didn’t want to ruin your day with gory pictures, we decided to enlighten it with some baby pictures. The purple markers with traffic accident detector activated is what the map would look like after CCTV feeds are integrated.
### Short Description
#### Problem
Cardiac arrest, heart attack, traumatic injuries-- the treatment of these conditions all have one thing in common. Time is the essence. If treated even a bit late, the patient can suffer from devastating permanent consequences and potentially even death.
#### How can technology help?
Our project aims to utilize CCTV infrastructure to detect emergency medical situations automatically (e.g. cardiac arrest or car crash) and contact EMS immediately with the location and symptom information. This not only allows SCDF to deliver a more timely and efficient response to emergency situations, but also allows them to assist vulnerable cohorts (e.g. elderly with no next to kin) in need.
#### General Overview
Funnel uses existing infrastructures such as CCTVs and public cams to identify emergency situations as fast as possible. We use several different detectors-- pose, blood, traffic accident, and fire--to recognize danger. The information is then sent to a webpage that displays a custom map of Singapore to show where the emergency is occuring. Then, human reviewers will be able to access the information and decide whether to send it to 995 or 1777.

### Local Minima's Team Members
##### Alan Chang
##### Alex Hsia
##### Gary Kim
##### Yong Gi Roh

### Pitch Video Link: 
[![Video Link](http://img.youtube.com/vi/wgscROZJBu8/0.jpg)](http://www.youtube.com/watch?v=wgscROZJBu8)


### The Architecture

![Our Project's Architecture](docs/Project_Architecture_Final_v4.png)
1. A camera records a live video that is sent to the central processor.
2. The central processor opens the detector group softwares.
3. IBM Human Pose Estimator detects whether someone is injured or sick based on the pose (e.g. lying down motionless for too long).
4. The blood detector detects blood based on the color.
5. Traffic accident detector uses machine learning to identify traffic accidents.
6. Fire detector detects uses machine learning to look for fire in accident site.
7. The detector information is sent to the central processor and then to human reviewer for confirmation.
8. The human reviewer will contact EMS at the location through the web browser.
9. Local EMS will be dispatched.

### [Detailed Description](https://docs.google.com/document/d/1YqrppUyYvqs1jqTFJ0CxOdZnRa1BEf_VNqFxH6yRMlk/edit?usp=sharing)

### Live Demo <https://scdfxibm2020.garykim.dev>

### Getting Started

You will need to have Python 3, pip, Node, and NPM required. 

##### Clone the repo

```bash
git clone https://github.com/local-minima/LocalMinima-Funnel_SCDFXIBM
cd LocalMinima-Funnel_SCDFXIBM
```

##### Build and serve the frontend

```bash
npm install
npm run frontend:build
cd static
python3 -m http.server
```

After you have run these commands, you can access the frontend at http://localhost:8000.

##### Backend APIs

These are hosted on an IBM Cloud Virtual Server so you won't need to build these typically. If you still want to, you can run the following commands for each:

* Blood Detector

```bash
pip install -r requirements.txt && cd detectors/blood-detector && python blood_detector.py
```

* Traffic Accident Detector

```bash
pip install -r requirements.txt && cd detectors/traffic-accident && python detect_traffic.py
```

* Fire Detector

```bash
pip install -r requirements.txt && cd detectors/fire-detector && python detect_fire.py
```

* Clutching Chest Detector

```bash
pip install -r requirements.txt && cd detectors/body-position && python clutching_chest_detector.py
```

* Abnormal Body Position Detector

```bash
pip install -r requirements.txt && cd detectors/body-position && python main.py
```

### IBM Functions

**More info can be found [here](docs/IBM.md).**

Many of the components of this system relies on APIs that are being run on virtual servers on the IBM cloud infrastructure.

The following are API endpoints that are being run on IBM Cloud and are extensively used throughout this system.

* `https://scdfxibm2020.garykim.dev/traffic`
* `https://scdfxibm2020.garykim.dev/pose/model/predict`
* `https://scdfxibm2020.garykim.dev/fire`
* `https://scdfxibm2020.garykim.dev/body`
* `https://scdfxibm2020.garykim.dev/chest`
* `https://scdfxibm2020.garykim.dev/blood`

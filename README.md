# FaceRecognition Based Attendance System
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### What steps you have to follow??
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt(this will install required package for project)
-  Move the `config.toml` file present in the repository to the `C:\~\.streamlit\config.toml`by default the file doesn’t exist.
-  Run `main.py` file by typing the following command in the terminal `streamlit run main.py`

### Project flow & explaination
- After you run the project you have to register your face so that system can identify you, so click on register 
- After you click you have to enter your name and then click on `Register` check box
- Now once the camera appears click on `Capture Image` button A camera window will pop up and it will detect your Face and take Image. The captured photo is stored in the folder named `TrainingImages`.
- Then you have to click on `Mark Attendance` button, It will train the model and convert all the Image into numeric format so that computer can understand. we are training the image so that next time when we will show the same face to the computer it will easily identify the face.
- It will take some time(depends on you system).
- Your attendance will be appended to  `Attendance.csv` file
- You can view the attendance after clicking `View Attendance` button. It will show record in tabular format.

### Screenshots

### Simple UI Home Page
<img src='https://github.com/spoorti016/FaceRecognition/blob/main/AppScreenshots/1653785349099.jpg'>

### Register 
<img src='https://github.com/spoorti016/FaceRecognition/blob/main/AppScreenshots/1653785349000.jpg'>

## While taking Attendance
<img src='https://github.com/spoorti016/FaceRecognition/blob/main/AppScreenshots/1653785349020.jpg'>

## Attendance in tabular format 
<img src='https://github.com/spoorti016/FaceRecognition/blob/main/AppScreenshots/1653785349042.jpg'>

## project demonstration video link
https://drive.google.com/drive/folders/1hYkcR-NvTBYOSBJSgXSxCycg7LE70-S7

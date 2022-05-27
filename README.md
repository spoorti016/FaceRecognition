# FaceRecognition

### What steps you have to follow??
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt(this will install required package for project)
-  Run `main.py` file by typing the following command in the terminal `streamlit run main.py`


### Project flow & explaination
- After you run the project you have to register your face so that system can identify you, so click on register 
- After you click a small window will pop up in that you have to enter your name and then click on `Register` check box
- Now once the camera appears click on `Capture Image` button A camera window will pop up and it will detect your Face and take Image. The captured photo is stored in the folder named `TrainingImages`.
- Then you have to click on `Mark Attendance` button, It will train the model and convert all the Image into numeric format so that computer can understand. we are training the image so that next time when we will show the same face to the computer it will easily identify the face.
- It will take some time(depends on you system).
- Your attendance will be appended to  `Attendance.csv` file
- You can view the attendance after clicking `View Attendance` button. It will show record in tabular format.

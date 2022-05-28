import face_recognition
import numpy as np
import os
import cv2
import pandas as pd
import requests
import streamlit as st
from datetime import date
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu



st.markdown("<h1 style='text-align: center; color: white;'>Attendance System</h1>", unsafe_allow_html=True)

#navigation bar
nav = option_menu(None, ["Home","Register", "Mark Attendance", "View Attendance Sheet"],
    icons=['house','person-plus-fill', 'calendar2-check', "file-earmark-spreadsheet"],
    menu_icon="cast", default_index=0, orientation="horizontal")

#function to access json data of lottie animantion
def load_lotteiurl(url):
    r = requests.get(url)
    #if return is successful it will return a data score of 200
    if r.status_code!= 200:
        return None
    return r.json()



#---------Load Assests--------
lottie_register = load_lotteiurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")
lottie_faceRec = load_lotteiurl("https://assets7.lottiefiles.com/packages/lf20_43bodr9p.json")
lottie_attend = load_lotteiurl("https://assets7.lottiefiles.com/packages/lf20_Mnpusu.json")


#function that marks attendance into csv file
def markAttendance(name):

    df=pd.read_csv("Attendaance/Attendance.csv")
    entry = name.split('.')
    print(entry[0])
    split_name = entry[0]
    print(split_name)
    if split_name not in df.values:
        namelist = []
        namelist = {'NAME': [split_name]}
        df2 = pd.DataFrame(namelist)
        df = pd.concat([df, df2], ignore_index=True, axis=0)
        df.to_csv("Attendaance/Attendance.csv", index=False)
        print(df)
        if str(date.today()) in df.columns:
            for i in df.index:
                if df['NAME'][i] == name:
                    df.at[i, str(date.today())] = "absent"
        print(df)
    if str(date.today()) not in df.columns:
        df[str(date.today())]="absent"
        df.to_csv("Attendaance/Attendance.csv",index=False)
    for i in df.index:
        if  df['NAME'][i]== name:
            if df[str(date.today())][i]=="absent":
                df.at[i,str(date.today())]="present"
                df.to_csv("Attendaance/Attendance.csv",index=False)
                break


#creates face Encodings and returns its list
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#if user clicks on home tab
if nav == "Home":
    st_lottie(lottie_faceRec, height=300, key="register")
    st.write("\n \n")
    st.markdown('''<h2 style='text-align: center;color: white;'><u>How to use this website<u> </h2>''',unsafe_allow_html=True)
    st.write("###")
    img = Image.open('GUI_Images/flow chart (1).jpg')
    st.image(img)

#if user clicks on register tab
if nav == "Register":
    #imput user details
    # st.title("Register Yourself Here :pencil2:")
    st.markdown('''<h2 style='color: white;'><u>Register yourself here<u> </h2><i class="bi bi-journal-check"></i> ''', unsafe_allow_html=True)
    name = st.text_input("Enter Your Name : ","")
    if name!="":
        st.markdown(f"Welcome {name} :wave:")
        check = st.checkbox("Register")

        #when user checks the register option
        if check:
            run = st.button("Capture Image")
            if True:
                capture = cv2.VideoCapture(0)
                img_display = st.empty()

                while True:
                    ret,img = capture.read()

                    if run:
                        cv2.imwrite('TrainingImages\\{}.jpg'.format(name),img)
                        break
                    img_display.image(img,channels='BGR')
                capture.release()
                st.markdown("Registeration Successfull!")
                st_lottie(lottie_register,height=300,key="register")


#if user clicks on Mark Attendance tab
if nav == "Mark Attendance":
    st.title("Mark your Attendance")
    img="GUI_Images/attendance.jpg"
    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st_lottie(lottie_attend, height=300, key="register")
    with col2:
        st.markdown("Press mark button to mark your attendance")
        run = st.button("Mark")
        FRAME_WINDOW = st.image([])
        path = 'TrainingImages'
        images = []

        personName = []
        myList = os.listdir(path)

        for cur_img in myList:
            current_img = cv2.imread(f'{path}/{cur_img}')
            images.append(current_img)
            print(images)
            personName.append(os.path.splitext(cur_img)[0])
            print(personName)
            encodeListKnown = findEncodings(images)
        print("All Encodings Completed!!!")

        camera = cv2.VideoCapture(0)

        while run:
            ret, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = face_recognition.face_locations(faces)
            encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

            for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = personName[matchIndex]
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)

            if (cv2.waitKey(1) == ord('q')):
                break
            FRAME_WINDOW.image(frame)
        else:
            camera.release()
            st.write('Stopped')






# when user clicks on view attendance sheet
if nav == "View Attendance Sheet":
    st.markdown('''<h2 style='text-align: center;color: white;'><u>Attendance Sheet</u></h2>''',unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
       st.write("")
    with col2:
        df = pd.read_csv("Attendaance/Attendance.csv")
        st.dataframe(df)

    with col3:
        st.write("")


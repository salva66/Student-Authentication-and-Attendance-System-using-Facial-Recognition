from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Or Iris Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1390,height=45)

        img1=Image.open(r"layout_images\udom.jpg")
        img1=img1.resize((650,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=55,width=650,height=630)

        img2=Image.open(r"layout_images\recognition-banner.jpg")
        img2=img2.resize((950,700),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=650,y=55,width=950,height=630)

        #button

        b1_1=Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2", font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=365,y=500,width=300,height=40)

    # ========attendance ======================
    def mark_attendance(self,r,f,l,p):
        with open("attendance1.csv",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (f not in name_list) and (l not in name_list) and (p not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{f},{l},{r},{p},{dtString},{d1},Present")         


# ==============face recognition====================
    def face_recog (self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select FirstName from student where photoID="+str(id))
                f=my_cursor.fetchone()
               # f=str(f)
                f="+".join(f)

                my_cursor.execute("select LastName from student where photoID="+str(id))
                l=my_cursor.fetchone()
               # l=str(l)
                l="+".join(l)

                my_cursor.execute("select course from student where photoID="+str(id))
                p=my_cursor.fetchone()
                #p=str(p)
                p="+".join(p)

                my_cursor.execute("select reg_No from student where photoID="+str(id))
                r=my_cursor.fetchone()
                #r=str(r)
                r="+".join(r)


                if confidence>60:
                    cv2.putText(img,f"FName:{f}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"LName:{l}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"reg_No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Programme:{p}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(f,l,r,p)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"INELIGIBLE STUDENT",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()

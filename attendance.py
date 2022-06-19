from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
import os
import numpy as np
import time
from time import strftime
from datetime import datetime
import csv
from plyer import notification
from tkinter import filedialog
from playsound import playsound
import multiprocessing
 

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Or Iris Recognition System")

        # ======================variables=========================
        self.var_dep=StringVar()
        self.var_photoID=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_reg_No=StringVar()
        self.var_FirstName=StringVar()
        self.var_MiddleName=StringVar()
        self.var_LastName=StringVar()
        self.var_studentEmail=StringVar()
        self.var_DoB=StringVar()
        self.var_gender=StringVar()
        self.var_photo=StringVar()
        self.var_prog_codeL=StringVar()
        self.var_prog_codeN=StringVar()
        self.var_program=StringVar()
        self.var_course_name=StringVar()
        self.var_reg_Status=StringVar()
        self.var_reg_ID=StringVar()
        self.var_regi_ID=StringVar()
        self.var_status=StringVar()
        self.var_hours=StringVar()
        self.var_mins=StringVar()
        self.var_secs=StringVar()
        self.var_hours.set('00')
        self.var_mins.set('00')
        self.var_secs.set('00')
        



        title_lbl=Label(self.root,text="ATTENDANCE", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1390,height=45)

        # background image
        img3=Image.open(r"layout_images\cive.jpg")
        img3=img3.resize((1390,615),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=60,width=1390,height=615)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=10,width=1345,height=590)

        # supervision course information
        supervision_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Supervision Course Details",font=("times new roman",20,"bold"))
        supervision_course_frame.place(x=0,y=0,width=650,height=520)

        # supervising course
        supervising_label=Label(supervision_course_frame,text="Supervised Course:",font=("times new roman",25,"bold"))
        supervising_label.grid(row=0,column=0,padx=10,sticky=W)

        supervising_combo=ttk.Combobox(supervision_course_frame,textvariable=self.var_course_name,font=("times new roman",20,"bold"),state="readonly",width=17)
        supervising_combo["values"]=("Select Course","TN 430","CS 430","CP 222","IA 116")
        supervising_combo.current(0)
        supervising_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #def clock(self):
            #clock_time=strftime('%H:%M:%S')
            #currentTime_label.config(text=clock_time)
            #currentTime_label.after(1000,clock)

        # current time label
        #currentTime_label=Label(supervision_course_frame,text="Current Time:",font=("times new roman",25,"bold"))
        #currentTime_label.grid(row=2,column=0,padx=10,sticky=W)
        #clock(self)

        #timer
        examDuration_label=Label(supervision_course_frame,text="Exam Duration:",font=("times new roman",25,"bold"))
        examDuration_label.grid(row=1,column=0,padx=10,sticky=W)

        hrs_label=Label(supervision_course_frame,text="hours",font=("times new roman",13,"bold"))
        hrs_label.place(x=245,y=142)

        hrs_entry=ttk.Entry(supervision_course_frame,textvariable=self.var_hours,width=3,font=("times new roman",25,"bold"))
        hrs_entry.place(x=190,y=120)

        mins_label=Label(supervision_course_frame,text="mins",font=("times new roman",13,"bold"))
        mins_label.place(x=355,y=142)

        mins_entry=ttk.Entry(supervision_course_frame,textvariable=self.var_mins,width=3,font=("times new roman",25,"bold"))
        mins_entry.place(x=300,y=120)

        secs_label=Label(supervision_course_frame,text="secs",font=("times new roman",13,"bold"))
        secs_label.place(x=455,y=142)

        secs_entry=ttk.Entry(supervision_course_frame,textvariable=self.var_secs,width=3,font=("times new roman",25,"bold"))
        secs_entry.place(x=400,y=120)

        b1_2=Button(supervision_course_frame,text="START",command=self.timer,cursor="hand2", font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_2.place(x=200,y=200,width=230,height=40)

        #b1_3=Button(supervision_course_frame,text="RESET",command=self.resetTime,cursor="hand2", font=("times new roman",18,"bold"),bg="green",fg="white")
        #b1_3.place(x=200,y=250,width=230,height=40)

        b1_30=Button(supervision_course_frame,text="UNIVERSITY EXAM",command=self.exam_time,cursor="hand2", font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_30.place(x=200,y=350,width=230,height=40)

        

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ATTENDANCE",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=8,width=650,height=520)
    

        # attendance label
        attendance_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Attendance System",font=("times new roman",12,"bold"))
        attendance_frame.place(x=3,y=105,width=640,height=385)

        # buttons frame
        btn_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=125,width=635,height=360)
        

        importcsv_btn=Button(btn_frame,text="VIEW ATTENDANCE",width=17,command=self.importCSV,font=("times new roman",25,"bold"),bg="blue",fg="white")
        importcsv_btn.place(x=15,y=150,width=600,height=40)

        # perform facial recognition button
        #b1_1=Button(btn_frame,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2", font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=15,y=50,width=600,height=40)
        
        #b1_51=Button(btn_frame,text="exit",command=self.close,cursor="hand2", font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        #b1_51.place(x=15,y=250,width=600,height=40)


    def importCSV(self):
        os.startfile("attendance")
   

    def timer(self):
        times=int(self.var_hours.get())*3600 + int(self.var_mins.get())*60 + int(self.var_secs.get())

        f_lbl2=Label(self.root)
        f_lbl2.place(x=200,y=400,width=230,height=40)

        while times > -1:
            minute, second=(times//60, times %60)

            hour=0
            if minute>60:
                hour,minute=(minute//60,minute%60)

            self.var_secs.set(second)
            self.var_mins.set(minute)
            self.var_hours.set(hour)

            root.update()
            time.sleep(1)

            if (times==0):
                p=multiprocessing.Process(target=playsound,args=("around_the_world-atc-midi.wav",))
                p.start()
                self.var_secs.set("00")
                self.var_mins.set("00")
                self.var_hours.set("00")
            times -=1
    
    def resetTime(self):
        self.var_hours.set('00')
        self.var_mins.set('00')
        self.var_secs.set('00')

    def exam_time(self):
        self.var_hours.set('3')
        self.var_mins.set('00')
        self.var_secs.set('00')
        


    # to match details entered by supervisor to know who to perform supervision to
    def supervise(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT FirstName,MiddleName,LastName,course\
                            FROM course_details,student,student_rstatus,student_tstatus\
                            WHERE student.course=course_details.program AND course_details.course_name='CS430' AND student.Reg_No=student_rstatus.Reg_No \
                            AND student_rstatus.reg_status='Registered' AND student_rstatus.reg_ID=student_tstatus.regi_ID AND student_tstatus.statuus='Above'")

    
    


        #button

        

    # ========attendance ======================
    def mark_attendance(self,r,f,l,p):
        with open("attendance1.csv","r+",newline="\n") as f:
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
    running = True
    
    def face_recog (self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                #Face_recognition.supervise(self)

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


                if confidence>90:
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

    def close(self):
        root.destroy()

      
      




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
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


class Face_recognition:
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
        



        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
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

        

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
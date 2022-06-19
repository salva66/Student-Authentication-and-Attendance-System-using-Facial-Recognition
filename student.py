from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2
from email_validator import validate_email, EmailNotValidError
from tkcalendar import DateEntry
from datetime import date


class Student:
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
        

        # first image
        img=Image.open(r"layout_images\udom_logo.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"layout_images\recognition-banner.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"layout_images\udom.jpg")
        img2=img2.resize((390,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=390,height=130)

        # background image
        img3=Image.open(r"layout_images\cive.jpg")
        img3=img3.resize((1390,615),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1390,height=615)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1390,height=45)

        main_frame=Frame(bg_img, bd=2)
        main_frame.place(x=10,y=55,width=1335,height=540)

        # left label frame
        #left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        #left_frame.place(x=10,y=8,width=650,height=520)


        # image on the left label frame
        #img_left=Image.open(r"layout_images\udom_logo.jpg")
        #img_left=img_left.resize((500,130),Image.ANTIALIAS)
        #self.photoimg_left=ImageTk.PhotoImage(img_left)

        #f_lbl=Label(left_frame,image=self.photoimg_left)
        #f_lbl.place(x=0,y=0,width=500,height=130)


        # current course information
        current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=8,width=650,height=520)

        def pick_programme(h):
            if dep_combo.get()=="CSE":
                course_combo.config(value=CSE_progs)
                course_combo.current(0)
            if dep_combo.get()=="ETE":
                course_combo.config(value=ETE_progs)
                course_combo.current(0)
            if dep_combo.get()=="IST":
                course_combo.config(value=IST_progs)
                course_combo.current(0)

        # Department
        deps=["Select Department","CSE","ETE","IST"]

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,value=deps,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # bind combo boxes
        dep_combo.bind("<<ComboboxSelected>>", pick_programme)

        # Course
        CSE_progs=["BSc CE","BSc CS","BSc CNISE","BSc SE","BSc CSDFE"]
        ETE_progs=["BSc DCBE","BSc TE"]
        IST_progs=["BSc IS","BSc BIS","BSc HIS","MTA"]

        course_label=Label(current_course_frame,text="Programme",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,value=["Select Programme"],textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
               

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("SelectAcademicYear","2018/2019","2019/2020","2020/2021","2021/2022")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","Semester 1","Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




        # current course information
        #current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        #current_course_frame.place(x=14,y=135,width=640,height=120)
       
       # Class Student information
        class_student_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Class Student Details",font=("times new roman",12,"bold"))
        class_student_frame.place(x=14,y=135,width=640,height=390)

        #Registration number
        RegistrationNumber_label=Label(class_student_frame,text="Reg_Number:",font=("times new roman",12,"bold"))
        RegistrationNumber_label.grid(row=0,column=0,padx=10,sticky=W)

        RegistrationNumber_entry=ttk.Entry(class_student_frame,textvariable=self.va_reg_No,width=20,font=("times new roman",12,"bold"))
        RegistrationNumber_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        
        #First name
        FirstName_label=Label(class_student_frame,text="FirstName:",font=("times new roman",12,"bold"))
        FirstName_label.grid(row=0,column=2,padx=20,sticky=W)

        FirstName_entry=ttk.Entry(class_student_frame,textvariable=self.var_FirstName,width=20,font=("times new roman",12,"bold"))
        FirstName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Middle name
        MiddleName_label=Label(class_student_frame,text="MiddleName:",font=("times new roman",12,"bold"))
        MiddleName_label.grid(row=1,column=0,padx=20,sticky=W)

        MiddleName_entry=ttk.Entry(class_student_frame,textvariable=self.var_MiddleName,width=20,font=("times new roman",12,"bold"))
        MiddleName_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Last name
        LastName_label=Label(class_student_frame,text="LastName:",font=("times new roman",12,"bold"))
        LastName_label.grid(row=1,column=2,padx=20,sticky=W)

        LastName_entry=ttk.Entry(class_student_frame,textvariable=self.var_LastName,width=20,font=("times new roman",12,"bold"))
        LastName_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)


        #DoB       
        

        DoB_label=Label(class_student_frame,text="DateofBirth:",font=("times new roman",12,"bold"))
        DoB_label.grid(row=2,column=0,padx=20,sticky=W)

        dt1=date(1980,4,14)
        dt2=date(2004,12,31)
        DoB_entry=DateEntry(class_student_frame,selectmode='day',mindate=dt1,maxdate=dt2,textvariable=self.var_DoB,width=20,font=("times new roman",12,"bold"))
        DoB_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #dt=range(mindate=dt1,maxdate=dt2)
        DoB_entry.set_date(dt2)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=2,padx=20,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=19)
        gender_combo["values"]=("Select Gender","MALE","FEMALE")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #Student Email
        
        studentEmail_label=Label(class_student_frame,text="StudentEmail:",font=("times new roman",12,"bold"))
        studentEmail_label.grid(row=3,column=0,padx=10,sticky=W)

        studentEmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentEmail,width=20,font=("times new roman",12,"bold"))
        studentEmail_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #photoID
        photoID_label=Label(class_student_frame,text="photoID:",font=("times new roman",12,"bold"))
        photoID_label.grid(row=3,column=2,padx=10,sticky=W)

        photoID_entry=ttk.Entry(class_student_frame,textvariable=self.var_photoID,width=20,font=("times new roman",12,"bold"))
        photoID_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4, column=0)
     
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4, column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=240,width=635,height=36)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
    
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=635,height=36)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=8,width=650,height=520)

        # image on the right label frame
        #img_right=Image.open(r"layout_images\udom_logo.jpg")
        #img_right=img_right.resize((500,130),Image.ANTIALIAS)
        #self.photoimg_right=ImageTk.PhotoImage(img_right)

        #f_lbl=Label(right_frame,image=self.photoimg_right)
        #f_lbl.place(x=0,y=0,width=500,height=130)

        # =========search system=========

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=3,y=105,width=640,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"))
        search_label.grid(row=0,column=0,padx=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Reg_Number","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

        # ==================table frame======================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=180,width=640,height=315)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","photoID","year","course","semester","RegistrationNumber","FirstName","MiddleName","LastName","DoB","studentEmail","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("photoID",text="photoID")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("course",text="Programme")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("RegistrationNumber",text="Registration Number")
        self.student_table.heading("FirstName",text="FirstName")
        self.student_table.heading("MiddleName",text="MiddleName")
        self.student_table.heading("LastName",text="LastName")
        self.student_table.heading("DoB",text="DoB")
        self.student_table.heading("studentEmail",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="Photo Sample")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("photoID",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("course",width=150)
        self.student_table.column("semester",width=100)
        self.student_table.column("RegistrationNumber",width=100)
        self.student_table.column("FirstName",width=150)
        self.student_table.column("MiddleName",width=150)
        self.student_table.column("LastName",width=150)
        self.student_table.column("DoB",width=100)
        self.student_table.column("studentEmail",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        

    # =========================function declaration=======================
    def add_data(self):
        try:
            is_valid=validate_email(self.var_studentEmail.get())
            Student.woow(self)
        except EmailNotValidError as e:
            messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)
            print(str(e))
        
        
        
    def woow(self):
        if self.var_dep.get()=="Select Department" or self.var_FirstName.get()=="" or self.va_reg_No.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            
        
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_photoID.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.va_reg_No.get(),
                                                                                                self.var_FirstName.get(),
                                                                                                self.var_MiddleName.get(),
                                                                                                self.var_LastName.get(),
                                                                                                self.var_DoB.get(),
                                                                                                self.var_studentEmail.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_radio1.get()                             

                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)

            except Exception as es:
                    messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

            

    # ======================fetch data==============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =================get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_photoID.set(data[1]),
        self.var_year.set(data[2]),
        self.var_course.set(data[3]),
        self.var_semester.set(data[4]),
        self.va_reg_No.set(data[5]),
        self.var_FirstName.set(data[6]),
        self.var_MiddleName.set(data[7]),
        self.var_LastName.set(data[8]),
        self.var_DoB.set(data[9]),
        self.var_studentEmail.set(data[10]),
        self.var_gender.set(data[11]),
        self.var_radio1.set(data[12])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_FirstName.get()=="" or self.va_reg_No.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student setails",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set dep=%s,reg_No=%s,year=%s,course=%s,semester=%s,FirstName=%s,MiddleName=%s,LastName=%s,DoB=%s,studentEmail=%s,gender=%s,photo=%s where photoID=%s",(
                                                                                                self.var_dep.get(),
                                                                                                self.va_reg_No.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_FirstName.get(),
                                                                                                self.var_MiddleName.get(),
                                                                                                self.var_LastName.get(),
                                                                                                self.var_DoB.get(),
                                                                                                self.var_studentEmail.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_radio1.get(),
                                                                                                
                                                                                                self.var_photoID.get()
                                                                                            ))

                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Students details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # delete function
    def delete_data(self):
        if self.va_reg_No.get()=="":
            messagebox.showerror("Error","Student Registration Number is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where RegistrationNumber=%s"
                    val=(self.va_reg_No.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_photoID.set(""),
        self.var_year.set("SelectAcademicYear"),
        self.var_course.set("Select Programme"),
        self.var_semester.set("Select Semester"),
        self.va_reg_No.set(""),
        self.var_FirstName.set(""),
        self.var_MiddleName.set(""),
        self.var_LastName.set(""),
        self.var_DoB.set(""),
        self.var_studentEmail.set(""),
        self.var_gender.set("Select Gender"),
        self.var_radio1.set("")     

    # ========================Generate dataset or take photo SamPles ===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_FirstName.get()=="" or self.va_reg_No.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set dep=%s,reg_No=%s,year=%s,course=%s,semester=%s,FirstName=%s,MiddleName=%s,LastName=%s,DoB=%s,studentEmail=%s,gender=%s,photo=%s where photoID=%s",(
                                                                                                self.var_dep.get(),
                                                                                                self.va_reg_No.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_FirstName.get(),
                                                                                                self.var_MiddleName.get(),
                                                                                                self.var_LastName.get(),
                                                                                                self.var_DoB.get(),
                                                                                                self.var_studentEmail.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_radio1.get(),
                                                                                                self.va_photoID.get()==id+1
                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close

                # =================Load PreDefIned DaTa on face frontal from cvFaCe =================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    #scaling factor=1.3
                    #minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        conn=mysql.connector.connect(host="localhost",username="root",password="1Chibole",database="face_recognizer")
                        my_cursor=conn.cursor()
                        #my_cursor.execute("select photoID from student where RegistrationNumber=%s",self.var_photoID.get())
                        file_name_path="data/student."+str(id)+"."+str(img_id)+".jpg"
                        #file_name_path="data/student."+str(2)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        conn.commit()
                        self.fetch_data()
                        conn.close()

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

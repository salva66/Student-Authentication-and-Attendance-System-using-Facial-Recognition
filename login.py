from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        img3=Image.open(r"layout_images\cive.jpg")
        img3=img3.resize((1390,615),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1390,height=725)

        #self.bg=ImageTk.PhotoImage(file="D:\FOURTH YEAR\FYP\PROTO4\layout_images\cive.jpg")

        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=10,y=10,width=2000,height=1000)

        frame=Frame(self.root,bg='black')
        frame.place(x=410,y=170,width=540,height=450)

        img1=Image.open("D:\FOURTH YEAR\FYP\PROTO4\layout_images\login_icon.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=180,width=100,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=200,y=100)

        #lables
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=200,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=40,y=245)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=290,width=270)

        # ============icon images=========================
        #img2=Image.open("D:\FOURTH YEAR\FYP\PROTO4\layout_images\login_icon.jpg")
        #img2=img2.resize((25,25),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)
        #lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        #lblimg2.place(x=630,y=323,width=25,height=25)

        # login button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=340,width=120,height=30)

        # register button
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=50,y=380,width=120,height=30)

        #forgot password button
        #passbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        #passbtn.place(x=110,y=400,width=150,height=30)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get==():
            messagebox.showerror("Error", "all fields required")
        
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success","welcome to student authentication system")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1Chibole",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where mail=%s and pass=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    )
                                                                                    )
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            
            else:
                open_main=messagebox.askyesno("YesNo", "Access only authorized Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)

                else:
                    if not open_main:
                        return

            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variables=======================
        self.var_firstN=StringVar()
        self.var_middN=StringVar()
        self.var_lastN=StringVar()
        self.var_contact=StringVar()
        self.var_mail=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

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

        title_lbl=Label(bg_img,text="REGISTRATION SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1390,height=45)

        main_frame=Frame(bg_img, bd=2)
        main_frame.place(x=10,y=55,width=1335,height=540)

        # registration information
        registration_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="registration information",font=("times new roman",12,"bold"))
        registration_frame.place(x=10,y=8,width=1390,height=520)

        #First name
        FirstName_label=Label(registration_frame,text="FirstName:",font=("times new roman",12,"bold"))
        FirstName_label.grid(row=0,column=0,padx=20,sticky=W)

        FirstName_entry=ttk.Entry(registration_frame,textvariable=self.var_firstN,width=20,font=("times new roman",12,"bold"))
        FirstName_entry.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        #Middle name
        MiddleName_label=Label(registration_frame,text="MiddleName:",font=("times new roman",12,"bold"))
        MiddleName_label.grid(row=0,column=2,padx=20,sticky=W)

        MiddleName_entry=ttk.Entry(registration_frame,textvariable=self.var_middN,width=20,font=("times new roman",12,"bold"))
        MiddleName_entry.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        #Last name
        LastName_label=Label(registration_frame,text="LastName:",font=("times new roman",12,"bold"))
        LastName_label.grid(row=2,column=0,padx=20,sticky=W)

        LastName_entry=ttk.Entry(registration_frame,textvariable=self.var_lastN,width=20,font=("times new roman",12,"bold"))
        LastName_entry.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        #contact
        contact_label=Label(registration_frame,text="Contact:",font=("times new roman",12,"bold"))
        contact_label.grid(row=2,column=2,padx=20,sticky=W)

        contact_entry=ttk.Entry(registration_frame,textvariable=self.var_contact,width=20,font=("times new roman",12,"bold"))
        contact_entry.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        #Last name
        mail_label=Label(registration_frame,text="Email:",font=("times new roman",12,"bold"))
        mail_label.grid(row=4,column=0,padx=20,sticky=W)

        mail_entry=ttk.Entry(registration_frame,textvariable=self.var_mail,width=20,font=("times new roman",12,"bold"))
        mail_entry.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        #Password
        password_label=Label(registration_frame,text="Password:",font=("times new roman",12,"bold"))
        password_label.grid(row=4,column=2,padx=20,sticky=W)

        password_entry=ttk.Entry(registration_frame,textvariable=self.var_pass,width=20,font=("times new roman",12,"bold"))
        password_entry.grid(row=5,column=2,padx=10,pady=10,sticky=W)

        #Confirm Password
        confPass_label=Label(registration_frame,text="Confirm Password:",font=("times new roman",12,"bold"))
        confPass_label.grid(row=6,column=0,padx=20,sticky=W)

        confPass_entry=ttk.Entry(registration_frame,textvariable=self.var_confpass,width=20,font=("times new roman",12,"bold"))
        confPass_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        









if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

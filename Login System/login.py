from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
import os
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import requests


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


#---------------------- LOGIN PAGE ----------------------#
class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x1500+0+0")

        self.newpass = StringVar()
        #img = Image.open(r'C:\Users\Ritik Singhal\Desktop\Login System\p1.jpg')
        #img = img.resize((1550,800), Image.ANTIALIAS)
        #self.bg = ImageTk.PhotoImage(img)
        #lbl_bg = Label(self.root, image = self.bg)
        #lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        
        img1 = Image.open(r'C:\Users\Ritik Singhal\Desktop\Login System\p2.png')
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.UserImage = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image = self.UserImage, bg="black", borderwidth=0)
        lblimg.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame,text="Get Started", font=("times new roman",22,"bold"), fg="white", bg="black")
        get_str.place(x=95,y=100)

        # Labels
        username = Label(frame,text="Username", font=("times new roman",15), fg="white", bg="black")
        username.place(x=70,y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman",15))
        self.txtuser.place(x=40,y=190,width=270)


        password = Label(frame,text="Password", font=("times new roman",15), fg="white", bg="black")
        password.place(x=70,y=235)

        self.passuser = ttk.Entry(frame, font=("times new roman",15), show='*')
        self.passuser.place(x=40,y=270,width=270)

        img2 = Image.open(r'C:\Users\Ritik Singhal\Desktop\Login System\p3.png')
        img2 = img2.resize((28,28), Image.ANTIALIAS)
        self.Image2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image = self.Image2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=327, width=25, height=25)

        img3 = Image.open(r'C:\Users\Ritik Singhal\Desktop\Login System\p4.png')
        img3 = img3.resize((25,25), Image.ANTIALIAS)
        self.Image3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image = self.Image3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=405, width=25, height=25)

        # Buttons
        loginbtn = Button(frame,command = self.login,text="Login", font=("times new roman",15,"bold"), bd=3, relief=RIDGE, fg="white", bg="grey", activeforeground="white", activebackground="grey")
        loginbtn.place(x=110,y=320,width=120,height=35)

        registerbtn = Button(frame, command = self.register_window ,text="New User Register", font=("times new roman",10), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15,y=375,width=160)

        loginbtn = Button(frame, command=self.forgot_password_window ,text="Forgot Password", font=("times new roman",10), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10,y=395,width=160)
    
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    #------------------------------- RESET PASSWORD BUTTON ------------------------
    def reset_pass(self):
        if self.sques_entry.get() == "Select":
            messagebox.showerror("Error","Please Select Security Question",parent=self.root2)
        elif self.sans_entry.get() == "":
            messagebox.showerror("Error","Please Enter the Security Answer",parent=self.root2)
        elif self.new_pass.get() == "":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Ritik@MySql123",database="loginsystem")
            my_cursor = conn.cursor()
            query = ("select * from registrationtable where Email=%s and SecurityQues=%s and SecurityAns=%s")
            value = (self.txtuser.get(), self.sques_entry.get(), self.sans_entry.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please Enter Correct Ans",parent=self.root2)
            else:
                query = ("update registrationtable set Password=%s where Email=%s")
                value = (self.new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password updated successfully , Please Login",parent=self.root2)
                self.root2.destroy()        



    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error","Please Enter Username to Reset Password")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Ritik@MySql123",database="loginsystem")
            my_cursor = conn.cursor()
            query = ("select * from registrationtable where Email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            #print(row)

            if row == None:
                messagebox.showerror("Error","Please Enter Correct Username")
            else:
                conn.close()
                #------------------------- FORGOT PASSWORD PAGE --------------------------------
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x450+610+170")
                self.root2.configure(bg="grey")

                l = Label(self.root2,text="Reset Password", font=("times new roman",26,"bold"), fg="black", bg="grey" )
                l.place(x=0,y=10,relwidth=1)

                label5 = Label(self.root2, text="Select Security Question : ", font=("times new roman",17), bg="black", fg="white")
                label5.place(x=50,y=80)
                self.sques_entry = ttk.Combobox(self.root2, font=("times new roman",17), state="readonly")
                self.sques_entry["values"] = ("Select","Your Pet Name", "Your Nickname", "Your Favorite Dish")
                self.sques_entry.current(0)
                self.sques_entry.place(x=50,y=130,width=250)

                label6 = Label(self.root2, text="Security Answer : ", font=("times new roman",17), bg="black", fg="white")
                label6.place(x=50,y=180)
                self.sans_entry = ttk.Entry(self.root2,font=("times new roman",17))
                self.sans_entry.place(x=50,y=230,width=250)

                newpass = Label(self.root2, text="Enter New Password : ", font=("times new roman",17), bg="black", fg="white")
                newpass.place(x=50,y=280)
                self.new_pass = ttk.Entry(self.root2,font=("times new roman",17))
                self.new_pass.place(x=50,y=330,width=250)

                self.txt_newpass = Button(self.root2, command=self.reset_pass, text="Reset", font=("times new roman",17), bg="green", fg="white", activebackground="green", activeforeground="white")
                self.txt_newpass.place(x=145,y=385,width=100)



    def login(self):
        if self.txtuser.get()=="" or self.passuser.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            # Checking in Database
            conn = mysql.connector.connect(host="localhost",user="root",password="Ritik@MySql123",database="loginsystem")
            my_cursor = conn.cursor()
            query = ("select * from registrationtable where Email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Email Not Registered")
            else:
                query = ("select * from registrationtable where password=%s")
                value1 =  (self.passuser.get(),)
                my_cursor.execute(query,value1)
                row1 = my_cursor.fetchone()
                if row1 == None:
                    messagebox.showerror("Error","Incorrect Password")
                else:
                    messagebox.showinfo("Success","Login Successful")
                    self.root.destroy()
                    #weather.Tk()
                    #os.system('weather.py')    
               
            conn.commit()
            conn.close()            
                
 #------------ REGISTRATION FORM ------------------

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x800+0+0")
        self.root.configure(bg="grey")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityq = StringVar()
        self.var_securitya = StringVar()
        self.var_pass = StringVar()
        self.var_confirmpass = StringVar()

        label = Label(self.root,text="Registration Form", font=("arial",30,"bold"), bg="grey")
        label.place(x=600,y=50)

        #frame
        frame = Frame(self.root, bg="black")
        frame.place(x=370,y=130,width=800,height=600)

        #Entry Widgets
        label1 = Label(frame, text="First Name : ", font=("times new roman",20), bg="black", fg="white")
        label1.place(x=50,y=60)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman",17))
        fname_entry.place(x=50,y=100,width=270)

        label2 = Label(frame, text="Last Name : ", font=("times new roman",20), bg="black", fg="white")
        label2.place(x=420,y=60)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman",17))
        lname_entry.place(x=420,y=100,width=270)

        label3 = Label(frame, text="Contact No. : ", font=("times new roman",20), bg="black", fg="white")
        label3.place(x=50,y=160)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman",17))
        contact_entry.place(x=50,y=200,width=270)

        label4 = Label(frame, text="Email : ", font=("times new roman",20), bg="black", fg="white")
        label4.place(x=420,y=160)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman",17))
        email_entry.place(x=420,y=200,width=270)

        label5 = Label(frame, text="Select Security Question : ", font=("times new roman",20), bg="black", fg="white")
        label5.place(x=50,y=260)
        sques_entry = ttk.Combobox(frame, textvariable=self.var_securityq, font=("times new roman",17), state="readonly")
        sques_entry["values"] = ("Select","Your Pet Name", "Your Nickname", "Your Favorite Dish")
        sques_entry.current(0)
        sques_entry.place(x=50,y=300,width=270)

        label6 = Label(frame, text="Security Answer : ", font=("times new roman",20), bg="black", fg="white")
        label6.place(x=420,y=260)
        sans_entry = ttk.Entry(frame, textvariable=self.var_securitya, font=("times new roman",17))
        sans_entry.place(x=420,y=300,width=270)

        label7 = Label(frame, text="Password : ", font=("times new roman",20), bg="black", fg="white")
        label7.place(x=50,y=360)
        password_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman",17))
        password_entry.place(x=50,y=400,width=270)

        label8 = Label(frame, text="Confirm Password : ", font=("times new roman",20), bg="black", fg="white")
        label8.place(x=420,y=360)
        confirmpass = ttk.Entry(frame, textvariable=self.var_confirmpass, font=("times new roman",17), show="*")
        confirmpass.place(x=420,y=400,width=270)

        # CheckButton
        self.var_check = IntVar()
        chkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree Terms & Conditions", font=("times new roman",10), onvalue=1, offvalue=0)
        chkbtn.place(x=50,y=470)

        # Register Button
        img = Image.open(r"C:\Users\Ritik Singhal\Desktop\Login System\register.png")
        img = img.resize((210,145), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data ,image=self.photoimage,borderwidth=0,cursor="hand2",bg="black", activebackground="black")
        b1.place(x=275,y=485,width=200)

        # Back to login Button
        img1 = Image.open(r"C:\Users\Ritik Singhal\Desktop\Login System\back_to_login.png")
        img1 = img1.resize((80,50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, command = self.return_login ,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="black", activebackground="black")
        b2.place(x=525,y=470,width=100)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confirmpass.get():
            messagebox.showerror("Error","Password must be Confirmed Correctly",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions",parent=self.root)
        else:
            # Database Connectivity
            conn = mysql.connector.connect(host="localhost",user="root",password="Ritik@MySql123",database="loginsystem")
            my_cursor = conn.cursor()
            query = ("select * from registrationtable where Email=%s")
            value = (self.var_email.get(),) 
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already Registered . Go back to Login",parent=self.root)
            else:
                my_cursor.execute("insert into registrationtable values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securitya.get(),
                                                                                        self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful! , Proceed to Login",parent=self.root)
            self.root.destroy()

#------------------- Return To Login Button ----------------
    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
import os
from tkinter import messagebox
import mysql.connector


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
        b2 = Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="black", activebackground="black")
        b2.place(x=525,y=470,width=100)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get() != self.var_confirmpass.get():
            messagebox.showerror("Error","Password must be Confirmed Correctly")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions")
        else:
            # Database Connectivity
            conn = mysql.connector.connect(host="localhost",user="root",password="Ritik@MySql123",database="loginsystem")
            my_cursor = conn.cursor()
            query = ("select * from registrationtable where Email=%s")
            value = (self.var_email.get(),) 
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already Registered . Go back to Login")
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
            messagebox.showinfo("Success","Registration Successful!")                        


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
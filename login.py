import tkinter.messagebox as MessageBox
from tkinter import *

import pymysql
from PIL import Image, ImageTk

root = Tk()
root.title('Login page')
root.geometry('1366x768+100+10')
root.maxsize(1366, 768)
root.minsize(1366, 768)

f = "Calibri 25"


# --------function-------
def register():
    root.destroy()


def login():
    if e1.get() == "" or e2.get() == "":
        MessageBox.showerror("ERROR", "Please fill all the Fields")
    else:
        mycon = pymysql.connect(host="localhost", user="root", password="", db="regst")
        mycur = mycon.cursor()
        mycur.execute("select * from student where email=%s and pas=%s", (e1.get(), e2.get()))
        row = mycur.fetchone()
        if row is None:
            MessageBox.showerror("ERROR", "Invalid Email or Password")
        else:
            MessageBox.showinfo("SUCCESS", "Successfully Logged In")
            root.destroy()
        mycon.close()


# --------BACKGROUND DETAILS---------------
img = Image.open("images/wallpapersden.com_blue-digital-art-squares_1366x768.jpg")
photo = ImageTk.PhotoImage(img)
b_img = Label(root, image=photo)
b_img.place(x=0, y=0)

# ---------frame----------------
f1 = Frame(root, bg="#ffffff")
f1.place(x=300, y=130, height=500, width=800)

# -------LOGO----------
logo = Image.open("images/image.jpg")
photo1 = ImageTk.PhotoImage(logo)
icon = Label(root, image=photo1)
icon.place(x=300, y=130, height=500)

# ----------login details-------
name = Label(root, text="LOGIN HERE !", font="century 25 bold", bg="#ffffff", fg="blue")
name.place(x=730, y=150)

uname = Label(root, text="Email", font=f, bg="#ffffff")
uname.place(x=650, y=210)
e1 = Entry(root, font="arial 20", width=25, bg="#cccccc")
e1.place(x=650, y=260)

upass = Label(root, text="Password", font=f, bg="#ffffff")
upass.place(x=650, y=310)
e2 = Entry(root, font="arial 20", width=25, bg="#cccccc")
e2.place(x=650, y=360)

login = Button(root, text="LOGIN", font="century 20", width=13, bg="#000066", fg="white", command=login)
login.place(x=650, y=420)

l1 = Label(root, text="Don't  have  an  account?", fg="black", font="Calibri 17", bg="#ffffff")
l1.place(x=650, y=550)

regs = Button(root, text="REGISTER", font="Calibri 15", width=10, bg="#0000ff", fg="white", command=register)
regs.place(x=900, y=545)

root.mainloop()

from tkinter import *
import pymysql
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox
t=Tk()
t.title("Registration page")

t.geometry('1488x702+25+20')
t.maxsize(1488,702)
t.minsize(1488,702)

f=()

#--------BACKGROUND DETAILS---------------
img=Image.open("images/register_img.jpg")
photo=ImageTk.PhotoImage(img)
b_img=Label(t,image=photo)
b_img.place(x=0,y=0)

#--------------function------------
def register():
    if(f.get=="" or l.get()=="" or e.get()=="" or p.get()=="" or c.get()==""):
        MessageBox.showerror("ERROR","Please fill all the Fields")
    
    elif(p.get()!=c.get()):
        MessageBox.showerror("ERROR","Password and Confirmed Password should be same")

    else:
        first=f.get()
        last=l.get()
        email = e.get()
        pas=p.get()
        cpas=c.get()
        mycon = pymysql.connect(host="localhost",user="root",password="",db="regst")
        mycur = mycon.cursor()
        mycur.execute("insert into student(first,last,email,pas,cpas) values('"+first+"','"+last+"','"+email+"','"+pas+"','"+cpas+"')")
        mycon.commit()
        mycon.close()

        if(mycon):
            MessageBox.showinfo("SUCCEsS","Registered  Succesfully")
            t.destroy()
            import login
        #else:
         #   MessageBox.showerror("ERROR","Not Registered")


def reset():
    f.set("")
    l.set("")
    e.set("")
    p.set("")
    c.set("")

def back():
    t.destroy()
    import login

#----------registration details---------------
f=StringVar()
l=StringVar()
e=StringVar()
p=StringVar()
c=StringVar()

f1=Frame(t,bg="#ffffff")
f1.place(x=450,y=70,height=560,width=600)

name=Label(t,text="REGISTER HERE !",font="century 25 bold",bg="#ffffff",fg="blue")
name.place(x=580,y=90)

l1=Label(t,text="First Name",font="Calibri 20",bg="#ffffff")
l1.place(x=480,y=180)
t_l1=Entry(t,font="arial 20",width=20,bg="#cccccc",textvariable=f)
t_l1.place(x=690,y=180)

l2=Label(t,text="Last Name",font="Calibri 20",bg="#ffffff")
l2.place(x=480,y=230)
t_l2=Entry(t,font="arial 20",width=20,bg="#cccccc",textvariable=l)
t_l2.place(x=690,y=230)

l3=Label(t,text="Email",font="Calibri 20",bg="#ffffff")
l3.place(x=480,y=280)
t_l3=Entry(t,font="arial 20",width=20,bg="#cccccc",textvariable=e)
t_l3.place(x=690,y=280)

l4=Label(t,text="Password",font="Calibri 20",bg="#ffffff")
l4.place(x=480,y=330)
t_l4=Entry(t,font=f"arial 20",width=20,bg="#cccccc",textvariable=p)
t_l4.place(x=690,y=330)

l5=Label(t,text="Confirm password",font="Calibri 20",bg="#ffffff")
l5.place(x=480,y=380)
t_l5=Entry(t,font="arial 20",width=20,bg="#cccccc",textvariable=c)
t_l5.place(x=690,y=380)

b1=Button(t,text="Register",font=("century 20"),width=18,bg="#000066",command=register,fg="white")
b1.place(x=600,y=450)

b2=Button(t,text="Reset",command=reset,font=("century 20"),width=13,bg="#0000ff",fg="white")
b2.place(x=500,y=530)

b3=Button(t,text="Back",font=("century 20"),width=13,bg="#0000ff",fg="white",command=back)
b3.place(x=750,y=530)

t.mainloop()
from tkinter import*
from PIL import Image,ImageTk

rt=Tk()
rt.title('Welcome page')
rt.geometry('1290x800+150+0')
rt.maxsize(1290,800)
rt.minsize(1290,800)

#--------function---------
def btn1():
    rt.destroy()
    import chat_imp

def btn2():
    rt.destroy()
    import chat_doubts

#-------background---------
img=Image.open("images/wallpaper2you_245333.jpg")
photo=ImageTk.PhotoImage(img)
b_img=Label(rt,image=photo)
b_img.place(x=0,y=0)

title=Label(rt,text="WELCOME!",font="Castellar 45 bold",bg="#3ba5d7",fg="white")
title.place(x=450,y=40)

title=Label(rt,text='\n Hi! This is Bot-"Your Placement Guide". I am going to answer all your queries regarding your placements procedure and I will also answer the most important questions of your HR Interview Round. So, here you can chat and get your doubts  resolved.\n', wraplength="1300",bg="#2e7cba",fg="black",font="century 20 bold")
title.place(x=10,y=170)

pic=Image.open("images/360_F_400911587_8hmMcZE9Soxm5LS8xa9XbgyrHBc65334.jpg")
Photo=ImageTk.PhotoImage(pic)

l=Label(rt,text="Get Answers Of Placement Related Queries",bg="#204490",fg="white",font="Calibri 18 bold" )
l.place(x=100, y=500)
b1=Button(rt,image=Photo,bg="#20418e",command=btn1)
b1.place(x=180,y=555)

l1=Label(rt,text="Get Answers Of Importannt HR Questions",bg="#204490",fg="white",font="Calibri 18 bold" )
l1.place(x=750, y=500)
b2=Button(rt,image=Photo,bg="#20418e",command=btn2)
b2.place(x=830,y=555)


rt.mainloop()
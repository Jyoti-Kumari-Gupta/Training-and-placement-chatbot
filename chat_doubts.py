from tkinter import *
from PIL import Image, ImageTk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

root=Tk()

root.title('Chatbot')
root.geometry('500x600+400+50')
root.maxsize(500,600)
root.minsize(500,600)

bot=ChatBot("Bot")
trainer=ListTrainer(bot)

chat=[
    "Hi",
    "Hello my friend",
    "Hello",
    "Hey",
    "Hey",
    "Hello my friend",
    "Who are you?",
    "I'm chatterBot-Your placement guide",
    "How are you",
    "I'm fine. And I Hope the same to you too!",
    "How can we prepare for placement",
    "You need to prepare for Quantitative Aptitude,  Reasoning,  Verbal & Interview.",
    "How to prepare for placement",
    "You need to prepare for Quantitative Aptitude,  Reasoning,  Verbal & Interview.",
    "What are the syllabus of Quantitative aptitude?",
    "For aptitude you need to study maths which includes topics such as:-  Percentage,  Profit & Loss,  Time & Work,  Speed Time & Distance,  Permutation & Combination,  Simple Interest,  Compound Interest,  Mensuration,  Probability,  Average,  Ratio & Proportion,  Mixture & Alligation,  Simple Equation,  Problem on Numbbers,  Indices and Surds",
    "Syllabus of Quantitative aptitude?",
    "For aptitude you need to study maths which includes topics such as:-  Percentage,  Profit & Loss,  Time & Work,  Speed Time & Distance,  Permutation & Combination,  Simple Interest,  Compound Interest,  Mensuration,  Probability,  Average,  Ratio & Proportion,  Mixture & Alligation,  Simple Equation,  Problem on Numbbers,  Indices and Surds",
    "Syllabus of quant",
    "For quant you need to study maths which includes topics such as:-  Percentage,  Profit & Loss,  Time & Work,  Speed Time & Distance,  Permutation & Combination,  Simple Interest,  Compound Interest,  Mensuration,  Probability,  Average,  Ratio & Proportion,  Mixture & Alligation,  Simple Equation,  Problem on Numbbers,  Indices and Surds",
    "Correct time start preparation",
    "There is no fixed time to start. It may vary from person to person but as a BCA or Bsc-IT student where placements starts from 5th semester one is adviced to be prepared till that time.",
    "Syllabus for verbal test",
    "Passage/Sentence Rearrangement,  Error Detection & Correction,  Fill in the Blanks(icludes all parts of speech),  Comprehension Passages",
    "What is the syllabus for verbal test?",
    "Passage/Sentence Rearrangement,  Error Detection & Correction,  Fill in the Blanks(icludes all parts of speech),  Comprehension Passages",
    "What is the syllabus for reasoning?",
    "Series : Missing Numbers, Odd One Out,  Data Sufficiency,  Assumptions & Conclusions, Courses of Action,  Puzzles,  Syllogism,  Cubes,  Coding-Decoding",
    "Syllabus for reasoning?",
    "Series : Missing Numbers, Odd One Out,  Data Sufficiency,  Assumptions & Conclusions, Courses of Action,  Puzzles,  Syllogism,  Cubes,  Coding-Decoding",
    "How to start preparation?",
    "One must focus on his quatitative aptitude, verbal and resoning for their first round of placement and then on their technical skills and communication skills for their interview.",
    "How to prepare for interview?",
    "One must have command in atlest one programming language and have knowledge of their course whatever they have studied throughout their academics and it is  more beneficial to have a project included.",
    "Which programming languages should I learn?",
    "You can learn as many programming languages you want but make sure to master at least any one programming language of your choice. Recruiters only see whether you are able to code a given problem in any language of your choice (C, C++, Java etc.). We recommend you to master any one structured programming language like C and any one of the Object Oriented Programming language like C++, Java etc.",
    "How many programming languages should I learn?",
    "You can learn as many programming languages you want but make sure to master at least any one programming language of your choice. Recruiters only see whether you are able to code a given problem in any language of your choice (C, C++, Java etc.). We recommend you to master any one structured programming language like C and any one of the Object Oriented Programming language like C++, Java etc.",
    "Are projects important for placement?",
    "Projects lay a very vital role in your interview. It puts up a good impression on interviewers and also let them have an idea about your skills and your knowledge.",
    "How to contact a company about placement?",
    "You need to work out the best way to apply when you want to contact a placement company. You need to find whether the company has a career portal for job seekers on their website or not. You also require to figure out if they prefer meeting face-to-face or taking a telephonic interview.",
    "When should we start preparing for the placement test?",
    "There is no fixed time to start. It may vary from person to person but as a BCA or Bsc-IT student where placements starts from 5th semester one is adviced to be prepared till that time.",
    "How can I start my placement preparation?",
    "One must focus on his quatitative aptitude, verbal and resoning for their first round of placement and then on their technical skills and communication skills for their interview.",
    "What do we need to prepare for our interview?",
    "One must have command in atlest one programming language and have knowledge of their course whatever they have studied throughout their academics and it is  more beneficial to have a project included.",
    "What programming languages should I learn?",
    "You can learn as many programming languages you want but make sure to master at least any one programming language of your choice. Recruiters only see whether you are able to code a given problem in any language of your choice (C, C++, Java etc.). We recommend you to master any one structured programming language like C and any one of the Object Oriented Programming language like C++, Java etc.",
    "How much projects are important to be added in resume?",
    "Projects add a pinch of salt to your resume. Try to add 2-3 good projects with somehow description of 1-2 lines. Also, be prepared to deliver detail description of your project and also some of the corner scenarios your project should handle. While applying off-campus, try to include projects according to the technology on which company has vacancies because many companies have a resume filtering option. That is when you apply for a vacancy on their website your resume passes through an initial keyword matching process before it reaches to the hiring team.",
    "How do I contact a company about placement?",
    "You need to work out the best way to apply when you want to contact a placement company. You need to find whether the company has a career portal for job seekers on their website or not. You also require to figure out if they prefer meeting face-to-face or taking a telephonic interview.",
    "Does writing clean code increases the chance of getting selected?",
    "Writing clean code surely creates a good impression of you in front of the recruiter. Recruiters always prefer someone who can write code which is easily understandable and should also be efficient at the same time.",
    '',
    ''
]

trainer.train(chat)

#----------function-----------
def reply():
    if(entry.get()==""):
        msg="Please enter your question"
        l1.config(text=msg,fg="red")
    
    else:
        question=entry.get()
        question=question.capitalize()
        answer=bot.get_response(question)
        textarea.insert(END,"\n You: "+question+"\n")
        textarea.insert(END,"Bot: "+str(answer)+"\n")
        entry.delete(0,END)
        msg=""
        l1.config(text=msg,fg="red")

def clicker(event):
    send.invoke()

def bck():
    root.destroy()
    import welcome

bot=ChatBot("Bot")
trainer=ListTrainer(bot)


trainer.train(chat)

#--------logo-----------
top_frame=Frame(root,width=500,bg="#000066")
top_frame.pack()

img1=Image.open("images/images.png")
photo1=ImageTk.PhotoImage(img1)
back=Button(top_frame,image=photo1,bg="#000066",command=bck)
back.pack(anchor=NW,side=LEFT)

img=Image.open("images/robot-chatter-bot-say-hi-over-circuit-background-vector-19840344.jpg")
photo=ImageTk.PhotoImage(img)
b_img=Label(top_frame,image=photo,bg="#000066",width=480,height=100)
b_img.pack()

#----------main frame----------
main_frame=Frame(root,bd=4,bg="Black",width=500)
main_frame.pack()

scrollbar=Scrollbar(main_frame)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(main_frame,width=60,height=16,bd=4,font="century 14 italic",yscrollcommand=scrollbar.set,wrap="word")
textarea.pack()
scrollbar.config(command=textarea.yview)

#---------frame----------------
f1=Frame(root,bg="#000066")
f1.place(x=0,y=489,height=110,width=500)

entry=Entry(root,font="arial 15",bd=3)
entry.place(x=20,y=525,height=38,width=325)

send=Button(root,text="SEND",font=("Calibri 14 bold"),width=10,bg="#f9eae7",fg="#000066",command=reply)
root.bind("<Return>",clicker)
send.place(x=360,y=525)

msg=""
l1=Label(root,text=msg,font="arial 12 bold",bg="#000066")
l1.place(x=30,y=565)

root.mainloop()
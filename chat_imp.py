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

ques=[
    "Hi",
    "Hello my friend",
    "Hello",
    "Hey",
    "Who are you?",
    "I'm chatterBot-Your placement guide",
    "Tell us about yourself",
    "This is your big chance to make a good first impression. A brilliant answer here would be a professional snapshot of yourself – your core areas, studies and skills (according to the company concerned) and what you’re trying to achieve in your career. Briefly outline your personal life, but remember – the recruiters aren’t really interested in these things. Prepare a two-minute reply, which works as an ice-breaker and can lead directly towards the job / company you’re applying for.",
    "About yourself",
    "This is your big chance to make a good first impression. A brilliant answer here would be a professional snapshot of yourself – your core areas, studies and skills (according to the company concerned) and what you’re trying to achieve in your career. Briefly outline your personal life, but remember – the recruiters aren’t really interested in these things. Prepare a two-minute reply, which works as an ice-breaker and can lead directly towards the job / company you’re applying for.",
    "Introduce yourself",
    "This is your big chance to make a good first impression. A brilliant answer here would be a professional snapshot of yourself – your core areas, studies and skills (according to the company concerned) and what you’re trying to achieve in your career. Briefly outline your personal life, but remember – the recruiters aren’t really interested in these things. Prepare a two-minute reply, which works as an ice-breaker and can lead directly towards the job / company you’re applying for.",
    "Strength and weakness",
    "Questions about strengths and weaknesses are typical in interviews. All you have to do is to pick and emphasize strengths that are relevant to the job you’re applying for. As far as your weaknesses are concerned, choose to talk about those that are not very important for the job.",
    "What are your strength and weaknesses?",
    "Questions about strengths and weaknesses are typical in interviews. All you have to do is to pick and emphasize strengths that are relevant to the job you’re applying for. As far as your weaknesses are concerned, choose to talk about those that are not very important for the job.",
    "What are you doing to overcome your weaknesses?",
    "Keep it short and simple. Say that you are working hard to get rid of your weaknesses.",
    "What are your hobbies?",
    "State what excites you or something that you love doing the most in your free time. Remember – don’t lie. You will get caught out sooner or later and your prospective employer won’t be impressed if they find out that you had lied to them from the very start.",
    "Why should we hire you for this job?",
    "Tell the employer something unique about yourself, something other candidates can not offer.",
    "What would you consider as your biggest achievement till date?",
    "We all have achievements in life, big or small. Always remember to choose an achievement that is relevant to the job.",
    "Biggest achievement",
    "We all have achievements in life, big or small. Always remember to choose an achievement that is relevant to the job.",
    "What is your dream job?",
    "Be very cautious while answering this. Whatever you answer, try to align it with the job you have applied for. You can say, “I want to be in the senior management of this (XYZ) company and this job is the gateway for the same.” This will show your dedication and the interviewer would get an idea that you are someone who would like to stay.",
    " Where do you see yourself five years down the line?",
    "I would like to work hard and have a managing role in five years time. However, I understand that I need to learn a lot, and I believe that this position is a perfect starting point.” A great answer to impress the interviewer. It sort of builds a connection between your goals and the company.",
    "What motivates you?",
    " State something that you genuinely believe in. Also, link it with the role that you have applied for.",
    "Are you a team player?",
    "Never say a no. You always have to work with a team, irrespective of domain. A company would always like to have people who would work well in a team.",
    "Give us an example of a time when you handled a major crisis/difficult situation.You can talk about something that you handled well in pressure.",
    "What do you know about our organisation?",
    "Never say that a friend told me or your consultant told you about it. Give an impression to the recruiter that you knew about the company right from start and have done some solid research before coming. You can say that how you were always interested in advertising and “XYZ” company is what you always dreamt of.",
    "What do you know about us?",
    "Never say that a friend told me or your consultant told you about it. Give an impression to the recruiter that you knew about the company right from start and have done some solid research before coming. You can say that how you were always interested in advertising and “XYZ” company is what you always dreamt of.",
    "What salary are you expecting?",
    "While answering this question, try to emphasize that the money isn’t the deciding factor. And if you have a number in your mind, put it up in a smart way. It would be good to have some statistics to back it up.",
    "Are you willing/open to change in your role?",
    "It is smart and wise to keep your options open.",
    "Do you have any questions for us?",
    "It is always advised to ask some questions at the end of the interview. It shows that you are interested and you care about the job. Try not to be repetitive and ask something that has been discussed in the interview.Be sure to prepare yourself for these commonly asked questions but also be careful of any tricky questions that may come your way. Be cool and think before you answer and you’re sure to make a good impression with your prospective employer. Good luck!",
    "Which is your favourite subject?",
    "Your favourite subject or which subject you enjoy the most should be in sync with the job you are applying for. That means, keep two or three subjects in the pipeline which you can quote as your favourite subject and pick the one that goes best with the job profile as the right answer.",
    "Tell me something about yourself that is not on your resume?",
    "Here the interviewer is looking to know more about your personality and possibly evaluating culture fit, they want to see you as you are beyond your resume. Apart from your marks and internships and work experiences, what are the things that make you who you are and what that tells about what kind of an employee you will prove to be. \n In such a case, talk about one of your personal qualities that you might not have included in the resume, but that makes you a better candidate. If the job profile includes client interaction then you can talk about your exceptional oratory skills or you can highlight your problem solving skills if that is what the requirement is about. Similarly, you can focus on your work ethics to enrich your answer and impress the interviewer while moving beyond your resume. Quoting examples from your personal life can be a good practice while answering such questions.",
    "Have you taken part in extra-curricular activities?",
    "Do not talk about your hobbies here. There’s a difference between hobbies and extra-curricular activities. While hobbies are activities you do in your spare time, extra-curricular activities are activities you do at school/college-level where you have a certificate to back it up. It could be voluntary work like organizing an event or participating in sports, theatre and other competitions.",
    "What’s your greatest achievement?",
    "This need not always be academic achievement. It could be from your social life in the past too. Think and answer it.",
    "Are you an introvert or extrovert?",
    "Saying that you’re an introvert or an extrovert can classify you as an extreme, which is bad for you. When at work, your behavior needs to be as per the requirement. You can say that you behave as per the requirement and can be both.",
    "Do you have plans for further studies?",
    "This could be a tricky question to answer. If you answer with a yes, the company might feel that your further studies and work life may not complement each other. They might also feel that you would be working with them for a limited time. Be diplomatic here and say that you haven’t thought about it yet and will probably consider it after gaining some work experience in the industry and gaining some insights.",
    "Where do you see yourself 5 years from now?",
    "Learn about the industry you’re in and do an analysis. Talk to experienced professionals from the industry and understand it’s future as well as the growth pattern and how much time it’s going to take to get promoted from one position to another and whether you have the skills required. You need to be brutally honest with yourself here. If you don’t already have the skills, are you willing to develop them and how?",
    "What is success for you?",
    "Success is a subjective thing and can mean different things to different people. Don’t give them a cliched answer to this question. There’s not definitive answer to what success it, so tell them what it means to you.",
    "Why does this role interest you? why have you applied?",
    "This is asked to assess your interest levels in the role you’ve applied for. The interviewee wants to know if you’re really interested or have applied because you were jobless. Try and relate the job requirements with your candidature and explain to the interviewee why you’re suitable for the post.",
    "What skills do you want to develop to success in the role?",
    "Mention and talk about the roles necessary for the role you have applied for. This will show the interviewee that you’re ready to learn and also that you’re aware of your shortcomings. Tell them that, as a fresher, you have the ability to work hard but require a formal training to enhance the skills you have for professional environment.",
    "Are you willing to relocate in India?",
    "Answer this honestly and tell them if you have any plans to relocate in India and explain why.",
    "Do you mind working in shifts?",
    "You don’t have to agree just for the sake of it. Answer honestly and tell them if whether you’re ready to work in shifts or not. Mention if you have any inhibitions about working in shifts.",
    "Why do you want to join our organization?",
    "This is asked to check whether you have done your homework on the organization. Make sure you have read thoroughly about the organization through their website and social media and have gathered all their details before the interview. Tell them why you think their organization is great and how it is going to help you grow in your career.",
    "How long will you work for us?",
    "Every company knows that every professional working in their company will aspire a change as some point in their career. You could however, be diplomatic and tell them you haven’t thought about it or you could answer honestly too.",
    " Are you speaking to other companies too?",
    "Honestly answer this and say yes if you are",
    "Which companies?",
    "Don’t reveal the names of the companies. You can say that you respect the confidentiality of that company and you wouldn’t like to name them and say this politely.",
    "Why should we hire you?",
    "This is asked almost in every interview. You can talk about your greatest strengths here and link it with your job requirements. The company will hire you if they see that you can add value to the job. Tell them how your skills will help that position and about your ability to grasp things and learn quickly and your flexible attitude. These are some of the qualities interviewers look for in freshers.",
    "How soon can you join us?",
    "Think and answer this question and tell them frankly if you need time. Sometimes if you need to relocate for the job you will need some time for your commitments. A lot of freshers commit to an early joining date due to anxiety and face problems later. If you post-pone the joining it will give them a bad impression even before you join the company. Therefore give a practical answer.",
    "Interview Do’s",
    "1. Ask questions and be frank in your approach. 2.Be aware of the company’s profile and how well you can fulfil their requirement.3.Be Confident.Be comfortable while talking with your hand gestures.4.Be punctual and ensure that you reach at least 10 minutes early. 5.Bring a copy of all relevant documents. 6.Dress appropriately and look neat and clean. 7.Express yourself in simple words and clearly. 8.If you are being interviewed by a panel, ensure to make eye contact with the person who asks the question. 9.Be alert and listen to the questions and answer thoughtfully. 10.Present your skills in a positive light, even your weaknesses. 11.Make sure to fully understand the question and raise a question if you have a doubt about a certain statement. 12.In an interview, try to maintain the positive image that your CV has already created after the first round of short-listing. 13.Show enthusiasm for joining the company and the position.",
    "Interview Don’ts",
    "There are certain things to steer clear of. Go through them and ensure not to make these mistakes on your important day. 1. Don’t sit in a stiff posture. 2. Don’t answer questions with a simple “yes” or “no”. Make sure to explain your sentance on the statement. 3. Don’t dress casually or look untidy. 4. Don’t fidget while sitting. 5. Don’t interrupt the interviewer before they have finished asking a question. 6. Don’t lie when it comes to internship experiences and roles in the college. They can always cross-check. 7. Don’t make derogatory remarks about anyone, including your professors, supervisors, and fellow students.  8. Avoid asking too many questions about salary, holidays or bonuses. You may discuss these at length after an offer is made. 9. Don’t wear strong perfumes or fragrances.",
    "What is your ambition?",
    "Avoid generic statements like ‘I want to be a good manager’ or ‘I want to be a CEO in five years’. One can go for short-term and long-term ambitions. Try to make the answer explanatory and detailed so that the interviewer knows what plan one has charted out to achieve the bigger goal."
]

trainer.train(ques)

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

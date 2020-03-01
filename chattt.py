from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine=pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()



chatbot=ChatBot('Charlie',trainer='chatterbot.trainers.ListTrainer')

'''chatbot.train([
    "Hi, can i help you?",
    "Sure, I'd like to book a flight to England.",
    "Your flight has been booked."
    ])'''
conversation=[
    "hello",
    "hi there",
    "what is your name",
    "my name is bot "
    "how are you",
    "i am fine",
    "How are you",
    "What are you doing",
    "thank you",
    "Hi, can i help you?",
    "Sure, I'd like to book a flight to England.",
    "Your flight has been booked.",
    "what are you doing",
    "nothing,what are you doing",
    "in which language do you speak",
    "i am speaking in english!!"
    ]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

#response = chatbot.get_response('hi there')

#print(response)
#print("talk to bot ")
#while True:
    #query=input()
    #if query=='exit':
        #break
    #answer=chatbot.get_response(query)
    #print("bot :",answer)

main = Tk()
main.geometry("600x750")
main.title("navneet chatbot")
img = PhotoImage(file="chat3.png")

PhotoL = Label(main ,image=img)

PhotoL.pack(pady=5)

frame = Frame(main)


def lets_chatting_with_me():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END, "you :" + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot :",str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0 , END)
    msgs.yview(END)

sc = Scrollbar(frame)
msgs = Listbox(frame , width=80,height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT , fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana",20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Submit",font=("Verdana",20),command=lets_chatting_with_me)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key....

main.bind('<Return>',enter_function)

main.mainloop()

from gtts import gTTS
from tkinter import *
import pygame

answers = {
    "hi": "Hello",
    "bye": "Bye bye",
    "how are you?": "Thanks. how are you?",
    "what's your name?": "my name is robo,whats your name?",
    "whats your name?":"my name is robo,whats your name?",
    "nice ti meet you":"me too,i hope we will be good friends. "
}

player = pygame.mixer
player.init()
player.music.set_volume(0.7)
logs = 0

def answer_me():
    global logs
    logs += 1
    if e1.get() in answers:
        text = gTTS(answers.get(e1.get()), lang="en", tld="com")
    else:
        text = gTTS("I can't answer to you!", lang="en", tld="com")
    text.save(f'{logs}.mp3')
    player.music.load(f'{logs}.mp3')
    player.music.play()

# root = Tk()
# Button(root, text='play', command=answer_me).pack()
# e1 = Entry(root)
# e1.pack()
# root.mainloop()


r = Tk()
r.geometry("500x280")
Button(r, text='play', command=answer_me).pack()
e1 = Entry(r)
e1.pack()


eye=Button(r,bg='green',text=["."])
eye.place(x=70,y=20)


eye2=Button(r,bg='green',text=['.'])
eye2.place(x=390,y=20)

p = Button(r,bg="green",width=60,height=3,text="? ?")
p.place(x=20,y=100)

r.mainloop()
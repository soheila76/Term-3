from tkinter import *
from tkinter import filedialog
import pygame
def load():
    global player
    res=filedialog.askopenfilename()
    player=pygame.mixer
    player.init()
    player.music.load(res)
    player.music.set_volume(0.7)
    
def play():
    player.music.play()
    
def pause():
    player.music.pause()
    
def resume():
    player.music.unpause()
    
def stop():
    player.music.stop()
    
root=Tk()
root.title("♪♬  music player  ♪♬")
root.geometry("750x200")
load_btn=Button(root,text="load music ",width=10,height=3,bg="#CFFB93",command=load)
play_btn=Button(root,text="play music",width=10,height=3,bg="orange",command=play)
pause_btn=Button(root,text="pause music",width=10,height=3,bg="orange",command=pause)
resume_btn=Button(root,text="resume",width=10,height=3,bg="orange",command=resume)
stop_btn=Button(root,text="stop music",width=10,height=3,bg="orange",command=stop)
exit_btn=Button(root,text="exit",width=10,height=3,bg="#F26250",command=root.destroy)


#grid
load_btn.grid(row=2,column=0,pady=20,padx=8)
play_btn.grid(row=2,column=1,pady=20,padx=8)
pause_btn.grid(row=2,column=2,pady=20,padx=8)
resume_btn.grid(row=2,column=3,pady=20,padx=8)
stop_btn.grid(row=2,column=4,pady=20,padx=8)
exit_btn.grid(row=2,column=5,pady=20,padx=8)
root.mainloop()
from tkinter import *

def check(pp):
   win=Toplevel()
    
    
root=Tk()
root.geometry("500x500")

l1=Label(root,text="alaki").pack()
ent=Entry(root)

ent.bind("<Return>",check)
ent.pack()
root.mainloop()
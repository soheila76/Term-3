from tkinter import *
from tkinter import ttk

def check(pp):
    print(combo.get())
    
    
root=Tk()
root.geometry("500x500")

l1=Label(root,text="alaki").pack()
combo=ttk.Combobox(root,values=("boy","girl"))
combo.pack()

combo.bind("<<ComboboxSelected>>",check)

root.mainloop()
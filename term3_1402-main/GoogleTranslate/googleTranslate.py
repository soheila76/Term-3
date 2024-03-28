
from customtkinter import *
import tkinter as tk
import googletrans
from googletrans import Translator
from tkinter import ttk
app = CTk()

def get_text():
    global result_text
    text=user_text.get("1.0","end-1c")
    src=user_language.get()
    dest=result_language.get()
    if text != "":
        gt=Translator()
        result=gt.translate(text,dest=dest,src=src)
        output=result.text
        result_text.insert(tk.END,output)
        
#for get all languages that translate can support
list_languages=[]
all_languages=googletrans.LANGUAGES
for k,v in all_languages.items():
    list_languages.append(v)

app.geometry("600x400")

user_language=ttk.Combobox(app,values=list_languages,width=33)
result_language=ttk.Combobox(app,values=list_languages,width=33)
lbl1=tk.Label(app,text="Enter your text..",fg="white",bg="black")
lbl2=tk.Label(app,text="Translation..",fg="white",bg="black")
label2 = CTkLabel(app,text='Modern Login System UI')
user_text= tk.Text(app,height=10,width=35)
result_text= tk.Text(app,height=10,width=35)
button = CTkButton(app,text='Translate',command=get_text)



#grid
user_language.grid(row=0,column=0,pady=5)
result_language.grid(row=0,column=1,pady=5)
lbl1.grid(row=1,column=0,pady=10)
lbl2.grid(row=1,column=1,pady=10)
user_text.grid(row=2,column=0,padx=10)
result_text.grid(row=2,column=1)
button.grid(row=3,column=0,pady=15)
app.mainloop()
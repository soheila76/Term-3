from tkinter import *
from tkinter.ttk import Combobox

Reserved_List=[]

root = Tk()
data = {
    "a0":"not available",
    "a1":"Available",
    "a2":"Reserved",
    "a3":"not available",
    "b0":"not available",
    "b1":"Available",
    "b2":"Reserved",
    "b3":"Not available",
    "c0":"Available",
    "c1":"Reserved",
    "c2":"not available",
    "c3":"not available",
    "d0":"not available",
    "d1":"Available",
    "d2":"Reserved",
}
r=0
c=0
lf = LabelFrame(text="chairs ")
lf.pack(padx=20,pady=20)
ph = PhotoImage(file="chair.png")
for i in data.keys():
    if data[i]=="Available":
        b= "green"
    if data[i]=="not available":
        b= "red"
    if data[i]=="Reserved":
        b= "yellow"   
         
    Label(lf,text=i,bg=b,image=ph,compound="top").grid(row=r,column=c)  
    c +=1
    if c==4:
        c=0
        r+=1
available_chairs =[]     
for i in data.keys():
    if data[i]=="Available":
        available_chairs.append(i)
        
def Res():
    chair = c1.get()
    if chair[0]=="a":
        r=0
    elif chair[0]=="b":
        r=1
    elif chair[0]=="c":
        r=2
    elif chair[0]=="d":
        r=3
                
    Label(lf,text=chair,bg="yellow",image=ph,compound="top").grid(row=r,column=chair[1]) 
    available_chairs.remove(chair)
    Reserved_List.append(chair) 
    c1.config(values=available_chairs)
    c1.set("")
def finish():
    for i in Reserved_List:
        if i[0]=="a":
            r=0
        elif i[0]=="b":
            r=1
        elif i[0]=="c":
            r=2
        elif i[0]=="d":
            r=3
        Label(lf,text=i,bg="red",image=ph,compound="top").grid(row=r,column=i[1]) 

                
                    
def pay():
    PayWindow = Toplevel()
    PayWindow.geometry("300x300")
    pay_label1 = Label(PayWindow,text="you reserved :")
    pay_label1.pack()
    for i in Reserved_List:
        Label(PayWindow,text=i).pack()
    pay_label2 = Label(PayWindow,text=f"you should pay : {len(Reserved_List)*40}$")
    pay_label2.pack()
    pay_Button = Button(PayWindow,text="finish",command = finish)
    pay_Button.pack()

        
c1 = Combobox(root,values=available_chairs,state="readonly")
c1.pack(pady=10)

b1 = Button(root, text="Reserved",command=Res)
b2 = Button(root, text="Pay",command=pay)
b1.pack()       
b2.pack()       

root.mainloop()
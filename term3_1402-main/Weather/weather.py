#pip install tkintermapview
#pip install pyperclip
#pip install tkcalendar
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

import json
import datetime
import requests
from tkinter import *
import tkintermapview
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox

#-----------function-----------------
def weather():
    global f1
    f1.grid_forget()
    f1 = Frame(lf3,bg="#F6B563")
    f1.grid(row = 5,column = 0,padx=20)
    marker_1 = mymap.set_address(e1.get(), marker=True)
    marker_1.set_text(e1.get())
    day_get = cal.get_date().split("/")
    # print(day_get)
    day_y ="20"+str(day_get[2])
    if int(day_get[0])<10:
        day_m ="-0"+day_get[0]
    else:
        day_m ="-"+day_get[0]
    if int(day_get[1])<10 :
        
        day_d ="-0"+day_get[1]
    else:
        day_d ="-"+day_get[1]
    day = day_y+day_m+day_d
    # print(day)

    newurl = f"https://api.open-meteo.com/v1/forecast?latitude={marker_1.position[0]}&longitude={marker_1.position[1]}&hourly=temperature_2m"
    response_API = requests.get(newurl)
    # print(response_API.status_code)
    data = response_API.text
    all_data = json.loads(data)
    # print(all_data)
    t = 0
    # print("-----------------------------------------------------")
    for i in range(len(all_data["hourly"]["time"])):
        if day in all_data["hourly"]["time"][i]:
        
            day_weather = all_data["hourly"]["time"][i] , all_data["hourly"]["temperature_2m"][i]
            
            print(day_weather)
            Label(f1,text=day_weather,bg="#F6B563").grid(pady=3)
            t +=1
            if t==24:#counter for days hour
                t=0

    
# ----------MakeDays-----------------
date = datetime.datetime.now()

# ----------TK-----------------------
root = Tk()
root.geometry("1280x700")
root.config(bg="#F6B563")
#----------widgets-------------------
messagebox.showinfo("avaiable days : ","it can show weather forecast for today and next 6 days")
lf1  = LabelFrame(root,text="Map : ",bg="#F6B563")


lf2  = LabelFrame(root,text="info : ",bg="#F6B563")
lf3  = LabelFrame(root,text="weather : ",bg="#F6B563")


l1 = Label(lf2,text="City name :",bg="#F6B563")
e1 = Entry(lf2,width=22)
l2 = Label(lf2,text="Choose day :",bg="#F6B563")
cal= Calendar(lf2, selectmode="day",year= date.year, month=date.month, day=date.day)

b1 = Button(lf2,text="LookUp",command=weather)
f1 = Frame(lf3,bg="#F6B563")
#----------map-----------------------
mymap = tkintermapview.TkinterMapView(lf1,width=800,height=650)
mymap.set_address("Golsar Blvd, Rasht, Gilan Province,Iran")
mymap.pack()

# ------------grids -----------------
lf1.grid(row = 0,column = 0,padx = 30 , pady=30)
lf2.place(x=880,y = 30,height=670)
lf3.place(x=1200,y = 30,width=200,height=670)
l1.grid(row = 0,column = 0,padx=5,pady=20)
e1.grid(row = 1,column = 0,padx=20)
l2.grid(row = 2,column = 0,padx=5,pady=20)
cal.grid(row = 3,column = 0,padx=20)
b1.grid(row = 4,column = 0,padx=20,pady=20)
f1.grid(row = 5,column = 0,padx=20)
#------------end---------------------
root.mainloop()

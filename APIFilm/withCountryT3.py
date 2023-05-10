from tkinter import *
from tkinter import ttk
import requests
def getInfo():
    root.geometry("410x450")
    user_select_country=combo_country.get()
    result={}
    for i in apiresponse["data"]:
        if i["country"] == user_select_country:
            result=i
            print(result)
            print(result["title"])
            # lbl_result.config(text=f"Title:{i['title']}")

            lbl_result=Label(root,text=f"Title:{result['title']}",bg="#E7D4B5")
            lbl_result.grid(columnspan=2,pady=10)

response = requests.get("http://moviesapi.ir/api/v1/movies")
apiresponse=response.json()
countryList=[]
movieInfo=apiresponse["data"]

root=Tk()
root.config(bg="#E7D4B5")
root.geometry("410x150+1+1")
root.title("API")
lbl_country=Label(root,text="country",font=('Times',24),bg="#E7D4B5")

for i in range(len(movieInfo)):
    dic=movieInfo[i]
    if dic["country"] in countryList:
        pass
    else:
        countryList.append(dic["country"])
combo_country=ttk.Combobox(root,values=countryList,font=('Times',20))
print(f"Countrys names:{countryList}")
btn=Button(root,text="Enter",bg="#A0937D",width=9,height=3,command=getInfo)



#grid
lbl_country.grid(row=0,column=0,pady=10,padx=10)
combo_country.grid(row=0,column=1)
btn.grid(row=1,column=1,pady=15)
root.mainloop()
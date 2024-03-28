from tkinter import *
from tkinter import ttk
import requests
def getInfo():
    root.geometry("410x450")
    user_select_year=combo_year.get()
    result={}
    for i in apiresponse["data"]:
        if i["year"] == user_select_year:
            result=i
            print(result)
            print(result["title"])
            # lbl_result.config(text=f"Title:{i['title']}")

            lbl_result=Label(root,text=f"Title:{result['title']}",bg="#E7D4B5")
            lbl_result.grid(columnspan=2,pady=10)

response = requests.get("http://moviesapi.ir/api/v1/movies")
apiresponse=response.json()
yearList=[]
movieInfo=apiresponse["data"]

root=Tk()
root.config(bg="#E7D4B5")
root.geometry("410x150+1+1")
root.title("API")
lbl_year=Label(root,text="year",font=('Times',24),bg="#E7D4B5")

for i in range(len(movieInfo)):
    dic=movieInfo[i]
    if dic["year"] in yearList:
        pass
    else:
        yearList.append(dic["year"])
combo_year=ttk.Combobox(root,values=yearList,font=('Times',20))
print(f"year:{yearList}")
btn=Button(root,text="Enter",bg="#A0937D",width=9,height=3,command=getInfo)



#grid
lbl_year.grid(row=0,column=0,pady=10,padx=10)
combo_year.grid(row=0,column=1)
btn.grid(row=1,column=1,pady=15)
root.mainloop()
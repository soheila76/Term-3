from tkinter import *
from tkinter import ttk
import requests
def getInfo():
    root.geometry("410x450")
    user_select_title=combo_title.get()
    result={}

    for i in apiresponse["data"]:
        if i["title"] == user_select_title:
            result=i
            print(result)
            print(result["title"])

            lbl_result=Label(root,text=f"year:{result['year']} / genres:{result['genres']}",bg="#E7D4B5")
            lbl_result.grid(columnspan=2,pady=10)

response = requests.get("http://moviesapi.ir/api/v1/movies")
apiresponse=response.json()
titleList=[]
movieInfo=apiresponse["data"]

root=Tk()
root.config(bg="#E7D4B5")
root.geometry("410x150+1+1")
root.title("API")
lbl_title=Label(root,text="title",font=('Times',24),bg="#E7D4B5")

for i in range(len(movieInfo)):
    dic=movieInfo[i]
    if dic["title"] in titleList:
        pass
    else:
        titleList.append(dic["title"])
combo_title=ttk.Combobox(root,values=titleList,font=('Times',20))
print(f"title:{titleList}")
btn=Button(root,text="Enter",bg="#A0937D",width=9,height=3,command=getInfo)



#grid
lbl_title.grid(row=0,column=0,pady=10,padx=10)
combo_title.grid(row=0,column=1)
btn.grid(row=1,column=1,pady=15)
root.mainloop()
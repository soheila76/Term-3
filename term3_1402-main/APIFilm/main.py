from tkinter import *
from tkinter import ttk
import requests
def getInfo():
    topic=combo_topic.get()
    if topic != "":
        win=Toplevel()
        win.geometry("410x150+1+1")
        win.title("API")
        win.config(bg="#E7D4B5")
        # root.iconify()
        
        if topic == "genres":
            def getGenres():
                    win.geometry("410x450")
                    user_select_genres=combo_genres.get()
                    result={}
                    create_genres=''
                    for i in apiresponse["data"]:
                        create_genres=" ".join(i["genres"])
                        
                        if create_genres == user_select_genres:
                            print("yeeeeeeees")
                            result=i
                            print(result)
                            print(result["title"])
                            # lbl_result.config(text=f"Title:{i['title']}")

                            lbl_result=Label(win,text=f"Title:{result['title']}",bg="#E7D4B5")
                            lbl_result.grid(columnspan=2,pady=10)
            
            
            
            response = requests.get("http://moviesapi.ir/api/v1/movies")
            apiresponse=response.json()
            genresList=[]
            movieInfo=apiresponse["data"]
            lbl_country=Label(win,text="genres",font=('Times',24),bg="#E7D4B5")

            for i in range(len(movieInfo)):
                dic=movieInfo[i]
                if dic["genres"] in genresList:
                    pass
                else:
                    genresList.append(dic["genres"])
            combo_genres=ttk.Combobox(win,values=genresList,font=('Times',20))
            print(f"genres names:{genresList}")
            btn=Button(win,text="Enter",bg="#A0937D",width=9,height=3,command=getGenres)

            #grid
            lbl_country.grid(row=0,column=0,pady=10,padx=10)
            combo_genres.grid(row=0,column=1)
            btn.grid(row=1,column=1,pady=15)
        
        elif topic == "title":
            def getTitle():
                    win.geometry("410x450")
                    user_select_title=combo_title.get()
                    result={}

                    for i in apiresponse["data"]:
                        if i["title"] == user_select_title:
                            result=i
                            print(result)
                            print(result["title"])

                            lbl_result=Label(win,text=f"year:{result['year']} / genres:{result['genres']}",bg="#E7D4B5")
                            lbl_result.grid(columnspan=2,pady=10)
                            
            response = requests.get("http://moviesapi.ir/api/v1/movies")
            apiresponse=response.json()
            titleList=[]
            movieInfo=apiresponse["data"]

            lbl_title=Label(win,text="title",font=('Times',24),bg="#E7D4B5")

            for i in range(len(movieInfo)):
                dic=movieInfo[i]
                if dic["title"] in titleList:
                    pass
                else:
                    titleList.append(dic["title"])
            combo_title=ttk.Combobox(win,values=titleList,font=('Times',20))
            print(f"title:{titleList}")
            btn=Button(win,text="Enter",bg="#A0937D",width=9,height=3,command=getTitle)



            #grid
            lbl_title.grid(row=0,column=0,pady=10,padx=10)
            combo_title.grid(row=0,column=1)
            btn.grid(row=1,column=1,pady=15)
        
        elif topic == "country":
            def getCountry():
                    win.geometry("410x450")
                    user_select_country=combo_country.get()
                    result={}
                    for i in apiresponse["data"]:
                        if i["country"] == user_select_country:
                            result=i
                            print(result)
                            print(result["title"])

                            lbl_result=Label(win,text=f"Title:{result['title']}",bg="#E7D4B5")
                            lbl_result.grid(columnspan=2,pady=10)
                            
                            
            response = requests.get("http://moviesapi.ir/api/v1/movies")
            apiresponse=response.json()
            countryList=[]
            movieInfo=apiresponse["data"]


            lbl_country=Label(win,text="country",font=('Times',24),bg="#E7D4B5")

            for i in range(len(movieInfo)):
                dic=movieInfo[i]
                if dic["country"] in countryList:
                    pass
                else:
                    countryList.append(dic["country"])
            combo_country=ttk.Combobox(win,values=countryList,font=('Times',20))
            print(f"Countrys names:{countryList}")
            btn=Button(win,text="Enter",bg="#A0937D",width=9,height=3,command=getCountry)



            #grid
            lbl_country.grid(row=0,column=0,pady=10,padx=10)
            combo_country.grid(row=0,column=1)
            btn.grid(row=1,column=1,pady=15)
        
        elif topic == "year":
            def getYear():
                win.geometry("410x450")
                user_select_year=combo_year.get()
                result={}
                for i in apiresponse["data"]:
                    if i["year"] == user_select_year:
                        result=i
                        print(result)
                        print(result["title"])

                        lbl_result=Label(win,text=f"Title:{result['title']}",bg="#E7D4B5")
                        lbl_result.grid(columnspan=2,pady=10)
                        
                        
            response = requests.get("http://moviesapi.ir/api/v1/movies")
            apiresponse=response.json()
            yearList=[]
            movieInfo=apiresponse["data"]

            lbl_year=Label(win,text="year",font=('Times',24),bg="#E7D4B5")

            for i in range(len(movieInfo)):
                dic=movieInfo[i]
                if dic["year"] in yearList:
                    pass
                else:
                    yearList.append(dic["year"])
            combo_year=ttk.Combobox(win,values=yearList,font=('Times',20))
            print(f"year:{yearList}")
            btn=Button(win,text="Enter",bg="#A0937D",width=9,height=3,command=getYear)

            #grid
            lbl_year.grid(row=0,column=0,pady=10,padx=10)
            combo_year.grid(row=0,column=1)
            btn.grid(row=1,column=1,pady=15)
    
root=Tk()
root.config(bg="#E7D4B5")
root.geometry("410x150+1+1")
root.title("API")
lbl_country=Label(root,text="Select Topic",font=('Times',15),bg="#E7D4B5")

combo_topic=ttk.Combobox(root,font=('Times',20),values=('genres','title','country','year'))

btn=Button(root,text="Enter",bg="#A0937D",width=9,height=3,command=getInfo)



#grid
lbl_country.grid(row=0,column=0,pady=10,padx=10)
combo_topic.grid(row=0,column=1)
btn.grid(row=1,column=1,pady=15)
root.mainloop()
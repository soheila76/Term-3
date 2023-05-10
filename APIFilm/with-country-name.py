import requests
response = requests.get("http://moviesapi.ir/api/v1/movies")
apiresponse=response.json()

# ذخیره کشورهای موجود در ای پی آی درون یک لیست
countryList=[]

movieInfo=apiresponse["data"]
for i in range(len(movieInfo)):
    dic=movieInfo[i]
    if dic["country"] in countryList:
        pass
    else:
        countryList.append(dic["country"])
print(f"Countrys names:{countryList}")


user_select_country=input("Enter the name of a country that produced the movie:")

#چک کردن و مقایسه ورودی کاربر با مقدار موجود در ای پی آی
for i in apiresponse["data"]:
    if i["country"] == user_select_country:
        print(i)
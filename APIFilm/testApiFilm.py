import requests
response = requests.get("http://moviesapi.ir/api/v1/movies")
# print(response.status_code)
apiresponse=response.json()
# print(apiresponse)
countryList=[]

movieInfo=apiresponse["data"]
# print(movieInfo)

for i in range(len(movieInfo)):
    dic=movieInfo[i]
    print(dic)
    print("==================")
    if dic["country"] in countryList:
        pass
    else:
        countryList.append(dic["country"])

print(f"Countrys names:{countryList}")
# user_select_country=input("Enter the name of a country that produced the movie:")

# if user_select_country in countryList:
#     for i in movieInfo:
#         if movieInfo["country"] == movieInfo[user_select_country]:
#             print("==================")
#             print(user_select_country["title"])


# print(movieInfo)



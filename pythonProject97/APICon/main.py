import requests

def get_weather_update(city):
    params={
        "q":city,
        "units":"metric",
        "appid":"34d676c076a96a994006dd2305893888"
    }
    response=requests.get("https://api.openweathermap.org/data/2.5/weather",params=params)
    if response.status_code==200:
        data=response.json()
        print("Temp: ",data["main"]["temp"])
        print("Desc :",data["weather"][0]["description"])

get_weather_update("New York")



# access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNzA4M2FjMTAyNDQxZTI1ZTc3Mjc0ODkyYjlkNDBhMSIsIm5iZiI6MTc3MDgxNzExNC40NjIwMDAxLCJzdWIiOiI2OThjODY1YTBkN2EzN2Y0Mzg2N2U5N2UiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.KrGAqc6HNEvV9mqgRgfaD8vL_CRPAFus1sSZay2M26M"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
# url = "https://api.themoviedb.org/3/search/movie"
# response=requests.get(url,headers=headers,params={"query":"Titanic"})
# print(response.status_code)
# data=response.json()
# print(data)





# payload={
#     "userId":1,
#     "title":"mytry",
#     "body":"asdsfsdfsdfsdfsd"
# }
# response=requests.post("https://jsonplaceholder.typicode.com/posts",
#                        json=payload)
# print(response.status_code)
# print(response.json())




# import sqlite3
# response=requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# data=response.json()
# with sqlite3.connect("mydata.db") as conn:
#     cmd="insert into posts values(?,?,?)"
#     lst=[]
#     for row in data:
#         lst.append((row["id"],row["title"],row["body"].lower()[:70]))
#     conn.executemany(cmd,lst)
#     conn.commit()


# for row in data:
#     print(row["id"],"          ",row["title"])


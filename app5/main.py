from email import message
from urllib import request
import requests as rq
from send_email import send_mail

topic="tesla"

api_key="4ef4d06f978b49cba9d600162d7287c2"

url=f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=4ef4d06f978b49cba9d600162d7287c2&language=en"


request=rq.get(url)

content=request.json()
str="Subject: Today's News on Tesla From NewsApi\n\n"
news_count=0

for article in content["articles"]:
   if article["title"] and article["description"] and news_count<=19:
        try:
            str += article["title"].upper().encode('ascii').decode() + \
                    ":\n\n" + article["description"].encode('ascii').decode() +\
                        "\nFor more:"+article["url"]+3*"\n"
            news_count+=1
        except UnicodeEncodeError:
            continue


# with open("news.txt","w") as file:
#     file.writelines(str)

send_mail(str)

print("sent successfulll!!")
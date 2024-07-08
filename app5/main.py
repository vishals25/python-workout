from email import message
from urllib import request
import requests as rq
from send_email import send_mail

api_key="4ef4d06f978b49cba9d600162d7287c2"

url="https://newsapi.org/v2/everything?q=tesla&from=2024-06-08&\
sortBy=publishedAt&apiKey=4ef4d06f978b49cba9d600162d7287c2"

title=[]
message=[]

request=rq.get(url)

content=request.json()

for article in content["articles"]:
    title.append(article["title"])
    message.append(article["description"])



str=""

for i in range(0, len(title)):
    if title[i] and message[i]:
        try:
            title[i].encode('ascii')
            message[i].encode('ascii')
            str += title[i].upper() + ":\n\n" + message[i] + "\n\n\n"
        except UnicodeEncodeError:
            continue

send_mail(str)

print("sent successfulll!!")
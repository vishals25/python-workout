import requests
import time
import smtplib,ssl
import os
import selectorlib

import sqlite3 as sql

connection=sql.connect("data.db")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url="https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    # Create a new Accessor
    response=requests.get(url,headers=HEADERS)
    source=response.text
    return source


def extract(source):
    # Create a new Extractor
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value=extractor.extract(source)['tours']
    return value


def send_mail(message):
    host='smtp.gmail.com'
    port=465

    username ='svs15324@gmail.com'
    password = os.getenv("password1")

    receiver='svs15324@gmail.com'

    message=f"Subject: New Event Found..!\n"+message

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password) # type: ignore
        server.sendmail(username,receiver,message)
    print("Email Sent..!")



## Incase of Text File:##


# def store(value):
#     with open("data.txt","a") as file:
#         file.write(value+'\n')

# def read():
#     with open("data.txt","r") as file:
#         return file.read()



def store(value):
    row=value.split(",")
    row=[item.strip() for item in row]
    cursor=connection.cursor()
    cursor.execute("insert into events values (?,?,?)",row)
    connection.commit()

def read(value):
    row=value.split(",")
    row=[item.strip() for item in row]
    band,city,date=row
    cursor=connection.cursor()
    cursor.execute("select * from events where band=? and city=? and date=?", (band, city, date))
    rows=cursor.fetchall()
    return rows


if __name__=="__main__":

    ##Incase of Text File##
    # while True:
    #     source=scrape(url)
    #     value=extract(source)
    #     print(value)

    #     if value != "No upcoming tours":
    #         content=read()
    #         if value not in content:
    #             store(value)
    #             send_mail(value)
    #     time.sleep(20)

    while True:
        source=scrape(url)
        value=extract(source)
        print(value)

        if value != "No upcoming tours":
            row=read(value)
            if not row:
                store(value)
                send_mail(value)
        time.sleep(2)
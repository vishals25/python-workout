import smtplib,ssl

import os


def send_mail(message):
    host='smtp.gmail.com'
    port=465

    username ='svs15324@gmail.com'
    password = os.getenv("PASSWORD")

    receiver='svs15324@gmail.com'

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password) # type: ignore
        server.sendmail(username,receiver,message)
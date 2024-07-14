import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

import os


def send_mail(image):


    username ='svs15324@gmail.com'
    password = str(os.getenv("password1"))
    receiver='svs15324@gmail.com'

    host='smtp.gmail.com'
    port=465

    email_msg=EmailMessage()
    email_msg["Subject"]="Object Movement detected"
    email_msg.set_content("Hey, There is some movement at camera range !")
    
    with open(image, "rb") as file:

        content = file.read()

        maintype, subtype = mimetypes.guess_type(image)[0].split('/')  # type: ignore

        email_msg.add_attachment(content, maintype=maintype, subtype=subtype)



    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password=password) 
        server.send_message(email_msg, from_addr=username, to_addrs=receiver)

    print("Email Sent Successfully!")
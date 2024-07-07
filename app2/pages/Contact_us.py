import streamlit as s
from send_email import send_mail


s.header("Contact Me")


with s.form("contact_form",clear_on_submit= True):
   user_email=s.text_input(label="Your Email_Id:",placeholder="demo@gamil.com")
   message=s.text_area("your_message")

   message=f"""
    From:{user_email}
    {message}
    """

   submitted = s.form_submit_button("Submit")
   if submitted:
       send_mail(user_email,message)
       s.success("Will be Contacting You Soon !! Thank you")
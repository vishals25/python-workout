from numpy import record
import pandas as pd
import streamlit as st
from fpdf import FPDF
from streamlit_pdf_viewer import pdf_viewer
from sympy import true

st.set_page_config(page_title="Hotel Reservation",page_icon=":house_with_garden:")
st.header("Hotel Booking System")

# Load the hotel data
df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards=pd.read_csv("cards.csv",dtype=str).to_dict(orient="records") # type: ignore
df_cards_security=pd.read_csv("card_security.csv",dtype=str)


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        avail = df.loc[df["id"] == self.hotel_id, "available"]

        if len(avail) == 0:
            st.error("No availability information found for the given hotel_id.")
            return False
        elif len(avail) > 1:
            st.error("Multiple availability entries found for the given hotel_id.")
            return False
        
        # At this point, avail should be a single value
        avail = avail.squeeze()

        return avail == "yes"


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass



class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        pdf = FPDF("P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=20)
        pdf.set_text_color(44,44,44)
        pdf.cell(w=0, h=20, txt="Thank you for your reservation!", ln=1) # type: ignore
        pdf.cell(w=0, h=20, txt="Here are your details:", ln=1) # type: ignore
        pdf.set_font(family="Times", size=15)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=16, txt=f"Name: {self.customer_name}", ln=1) # type: ignore
        pdf.cell(w=0, h=16, txt=f"Hotel Name: {self.hotel.name}", ln=1) # type: ignore
        pdf.output("output.pdf")


class CreditCard:

    def __init__(self,card_number):
        self.card_number = card_number
    
    def validate(self,expiration,holder,cvc_number):
        card_data={"number": self.card_number,
                   "expiration": expiration,
                   "cvc": cvc_number,
                   "holder": holder
                   }
        if card_data in df_cards:
            return True
    
    def payment(self):
        return True
        

class SecureCreditCard(CreditCard):

    def authenticate(self,given_password):
        password=df_cards_security.loc[df_cards_security["number"]==self.card_number,"password"].squeeze()
        if password==given_password:
            return True



class SpaTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        pdf = FPDF("P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=20)
        pdf.set_text_color(44,44,44)
        pdf.cell(w=0, h=20, txt="Thank you for your Spa reservation!", ln=1) # type: ignore
        pdf.cell(w=0, h=20, txt="Here are your details:", ln=1) # type: ignore
        pdf.set_font(family="Times", size=15)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=16, txt=f"Name: {self.customer_name}", ln=1) # type: ignore
        pdf.cell(w=0, h=16, txt=f"Hotel Name: {self.hotel.name}", ln=1) # type: ignore
        pdf.output("outputspa.pdf")




# Streamlit app
st.sidebar.subheader("List Of Hotels:")
st.sidebar.write(df)
if True:
    hotel_id = st.text_input("Enter The Hotel Id:", placeholder="123", key="hotel_id")
    spa=st.text_input(label="Do you need A Spa Reservation?",placeholder='yes,no')
    if hotel_id:
        hotel = SpaHotel(hotel_id)
        if hotel.available():
            name = st.text_input(label="Enter Your Name:", placeholder='Alex', key="name")
            if name:
                card_number=st.text_input(label="Enter Credit CardNumber:",placeholder="1234 5678 9123 4567")
                expiration=st.text_input(label="Enter Expiration date",placeholder='12/26')
                holder=st.text_input(label="Enter Holder name:",placeholder="Alex")
                cvc_number=st.text_input(label="Enter CvC CardNumber:",placeholder="123")
                if card_number and expiration and holder and cvc_number:
                    credit_card=SecureCreditCard(card_number)
                    if credit_card.validate(expiration,holder,cvc_number):
                        password=st.text_input(label="Enter Password For Payment:")
                        if password:
                            if password!='':
                                valid_password=credit_card.authenticate(password)
                            else:
                                st.error("The password cannot be empty")
                        pay_btn=st.button(label="Payment")
                        if pay_btn:
                            if valid_password:
                                if credit_card.payment():
                                    reservation_ticket = ReservationTicket(name, hotel)
                                    spa_ticket=SpaTicket(name,hotel)
                                    reservation_ticket.generate()
                                    pdf_viewer("output.pdf",height=300)
                                    with open("output.pdf", "rb") as file:
                                        st.download_button(
                                            label="Download PDF",
                                            data=file,
                                            file_name="reservation_ticket.pdf",
                                            mime="application/octet-stream"
                                        )
                                    if spa.lower()=="yes":
                                        st.subheader(f"Spa Reservation")
                                        hotel.book_spa_package()
                                        spa_ticket.generate()
                                        pdf_viewer("outputspa.pdf",height=300)
                                        with open("outputspa.pdf", "rb") as file:
                                            st.download_button(
                                                label="Download PDF",
                                                data=file,
                                                file_name="spa_reservation_ticket.pdf",
                                                mime="application/octet-stream"
                                            )
                                    hotel.book()
                                    st.success("Reservation complete! You can download your tickets above")
                                else:
                                    st.error("Payment Failed")
                            else:
                                st.error("Password Verification are Unsuccessfull")
                    else:
                        st.error("Card Verification are Unsuccessfull")
        else:
            st.error("Hotel is unavailable..!")

st.text("double click to reset")
if st.button("Reset"):
    st.session_state.submitted = False
    st.experimental_rerun()
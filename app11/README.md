# Hotel Booking System

This is a simple Hotel Booking System built using Streamlit, designed to facilitate hotel reservations and payments.

## Features

- View a list of available hotels and their details.
- Book a hotel room by providing customer information and credit card details.
- Generate a reservation ticket in PDF format.
- Download the reservation ticket for offline access.
- Secure authentication for credit card payments.

## Requirements

- Python 3.x
- Pandas
- Streamlit
- FPDF
- Streamlit PDF Viewer

## Usage

1. Launch the Streamlit app by running `streamlit run app.py`.
2. Select a hotel from the sidebar list using its `hotel_id`.
3. Enter customer details (name) and credit card information (number, expiration, holder, cvc).
4. Authenticate the credit card with a password stored in `card_security.csv`.
5. Click the "Payment" button to confirm the reservation.
6. Upon successful payment, a reservation ticket in PDF format will be generated and displayed.
7. Optionally, download the PDF reservation ticket using the download button provided.

## Architecture

- **app.py**: Main Streamlit application script handling UI interactions and backend logic.
- **hotels.csv**: CSV file containing hotel data (id, name, available status).
- **cards.csv**: CSV file storing credit card information.
- **card_security.csv**: CSV file storing secure credit card information including passwords.

## Security Considerations

- Ensure secure handling of sensitive information such as credit card details.
- Use HTTPS for deployment to encrypt data in transit.
- Implement password hashing and secure storage practices for user passwords.

## Attachments

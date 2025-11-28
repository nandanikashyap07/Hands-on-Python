import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "Enter Your E-mail"
APP_PASSWORD = "Enter Your G-mail App Password"
RECEIVER = "Enter Receiver's E-mail"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello from PYTHON..."
msg.set_content("This email was sent using Python code!")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

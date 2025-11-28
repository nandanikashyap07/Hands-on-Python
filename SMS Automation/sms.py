from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

sid = os.getenv("TWILIO_SID")
token = os.getenv("TWILIO_TOKEN")
twilio_num = os.getenv("TWILIO_NUMBER")
target_num = os.getenv("RECEIVER_NUMBER")

client = Client(sid, token)

msg = client.messages.create(
    body="Hey, this is a test message sent through Python + Twilio.",
    from_=twilio_num,
    to=target_num
)

print("Message ID:", msg.sid)

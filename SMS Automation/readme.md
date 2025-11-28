# Twilio SMS Automation (Python)

This project is a lightweight Python tool that lets you send SMS messages through the Twilio API. It’s ideal for anyone learning how APIs work or for quick message automation from a Python script.

🚀 Highlights

Send SMS to any Twilio-approved mobile number

Uses Twilio’s official Python library

Short, clean, and beginner-friendly code

Keeps credentials secure using environment variables

Takes only a couple of minutes to set up and start sending messages

🛠️ Technologies

Python

Twilio REST API

python-dotenv (optional, for managing secrets)

📦 Getting Started

1. Clone the project

git clone https://github.com/your-username/twilio-sms-sender.git
cd twilio-sms-sender


2. Install the required packages

pip install twilio python-dotenv

🔐 Configure Your Environment

Avoid putting credentials in your code.
Create a file named .env and add your Twilio details:

TWILIO_SID=your_account_sid
TWILIO_TOKEN=your_auth_token
TWILIO_NUMBER=your_twilio_phone_number
RECEIVER_NUMBER=receiver_phone_number

🧩 What the Script Does

Loads your Twilio keys from environment variables

Builds a Twilio client instance

Sends an SMS using the client

Displays the message SID so you know it was processed

⚠️ Things to Keep in Mind

Trial accounts can only send messages to verified numbers

Not all Twilio numbers support sending SMS to Indian carriers

If your token gets exposed, generate a new one immediately

Never upload your .env file — keep it private

⭐ Support the Project

If you found this script helpful, drop a ⭐ on the repository!

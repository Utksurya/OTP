from twilio.rest import Client
import math
import random
import smtplib
import re

account_sid = 'AC7be53a6097ce248ec75a9d464ff2c721'
auth_token = '6c940aa4f51be729ecbdd1c7c453beb8'
input_no = '+19892782081'

def validate_mobile_no(mobile_no):
    return len(mobile_no) == 10 and mobile_no.isdigit()

def validate_email(email):
    validation_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(validation_condition, email):
        return 1
    else:
        return 0

def generate_otp():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random()*length)]

    return otp

def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # transfer layer security
    server.login('suryautkarsh1919@gmail.com', 'ekmkmqhcawuqdebi')
    message = 'Your 6 digit OTP is '+str(otp)
    server.sendmail('suryautkarsh1919@gmail.com',email, message)
    server.quit()

def send_otp_over_mobile(mobile_no, otp):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+otp,
        from_=input_no,
        to='+91'+str(mobile_no),
    )
    print(Message.body)

otp = generate_otp()

mobile_no = input("Enter the Mobile number:")
if (validate_mobile_no(mobile_no)):
    send_otp_over_mobile(mobile_no, otp)
else:
    print("Invalid Mobile no")

email = input("Enter the Email:")
if (validate_email(email)):
    send_email(email, otp)
else:
    print("Invalid Email ")
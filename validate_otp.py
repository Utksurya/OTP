from twilio.rest import Client
import math
import smtplib
import random
import re

account_sid = 'AC7be53a6097ce248ec75a9d464ff2c721'
auth_token = '6c940aa4f51be729ecbdd1c7c453beb8'
input_no = '+19892782081'

def validate_mobile_no(Mobile_no):
    return len(Mobile_no) == 10 and Mobile_no.isdigit()

def validate_email(email):
    validating_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.search(validating_condition, email):
        return True
    else:
        return False

def generate_otp():
    otp = ''.join([str(random.randint(0,9))for i in range(6)])

    return otp
def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() 
    server.login('suryautkarsh1919@gmail.com', 'ekmkmqhcawuqdebi')
    message = 'Your 6 digit OTP is '+str(otp)
    server.sendmail('suryautkarsh1919@gmail.com', email, message)
    server.quit()


def send_otp_through_sms(mobile_no, otp):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+otp,
        from_=input_no,
        to='+91'+str(mobile_no),
    )
    print(Message.body)


if __name__ == "_main_":

    otp = generate_otp()
    mobile_no = input("Enter the Mobile number:")
    if (validate_mobile_no(mobile_no)):
        send_otp_through_sms(mobile_no, otp)
    else:
        print("Invalid Mobile no")

    email = input("Enter the Email:")
    if (validate_email(email)):
        send_email(email, otp)
    else:
        print("Invalid Email ")
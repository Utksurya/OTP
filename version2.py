import random
import smtplib

account_sid = 'AC87d29f1bf3374f2067a057ddd8d8dd5e'
auth_token = '529385f4eb86b890cb0ce9268e61ddc9'

twilio_number = '+14705163287'
target_number = '+919552650041'

def generateOTP():
    otp = ''.join([str(random.randint(0,9)) for i in range(4)])
    return otp


def sendOTPOverEmail(email, otp):
    if validateEmail(email):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('nihalsathawane2003@gmail.com', 'exgf spgh lmwn swie')
        msg = 'Hello, your OTP is '+ str(otp) +  '\nPlease do not share the OTP with anyone.' +  '\nThis is System generated mail so do not reply.'
        server.sendmail("nihalsathawane2003@gmail.com","shreyasdeshingkar@gmail.com",msg)
        print(f"OTP is sent to email via email.")
    else:
        print("Invalid email address.")


def sendOTPOverMobile(mobile, otp):
    if validateMobile(mobile):
        
        from twilio.rest import Client
        import keys

        client = Client(keys.account_sid,keys.auth_token)
        msg = client.messages.create(

            body = 'Hello, your OTP is '+ str(otp) +  '\nPlease do not share the OTP with anyone.' +  '\nThis is System generated mail so do not reply.',
            from_ = keys.twilio_number,
            to = keys.target_number  
        )
        

        print(msg.body)
    else:
        print("Invalid mobile number.")


def validateEmail(email):
    
    if "@gmail" in email and "." in email:
        return True
    else:
        return False


def validateMobile(mobile):
    
    if len(mobile) == 10 and mobile.isdigit():
        return True
    else:
        return False


if __name__ == "__main__":
    
    otp = generateOTP()

    
    email = "shreyasdeshingkar@gmail.com"
    sendOTPOverEmail(email, otp)

    
    mobile = "9552650041"
    sendOTPOverMobile(mobile, otp)

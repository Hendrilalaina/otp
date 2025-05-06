import os
import math
import random
import smtplib
from dotenv import load_dotenv

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
msg = OTP + " is your OTP!"
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
load_dotenv()
s.login(os.getenv("EMAIL"), os.getenv("PASSWD"))
email_id = input("Enter your email: ")
s.sendmail("&&&&&&&&", email_id, msg)
a = input("Enter your otp: ")
if a == OTP:
    print("Verified!")
else:
    print("Please check your OTP again!")
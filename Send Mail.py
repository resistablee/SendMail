import smtplib
import ssl
import os
from email.message import EmailMessage

mail = input("Your mail address: ")
passw = input("Your mail password: ")
os.system("clear")
targetmail = input("Target mail adress: ")
subject = input("Subject: ")
context = input("Context: ")

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = mail
msg["To"] = targetmail
msg.set_content(context)

smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

try:
    smtp.login(mail, passw)
except smtplib.SMTPAuthenticationError:
    print("Authentication Error")

try:
    smtp.send_message(msg)
except smtplib.SMTPSenderRefused:
    print("The sender refused to send.")
except smtplib.SMTPRecipientsRefused:
    print("No recipients found.")
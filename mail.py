import smtplib
from keys import *
from email.message import EmailMessage

def send_email(rcvr,sub,msg):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('halimaafrooz@gmail.com',e_pass)
    email=EmailMessage()
    email['From']='halimaafrooz@gmail.com'
    email['To']= rcvr
    email['Subject']=sub
    email.set_content(msg)
    server.send_message(email)

email_list={
    'dude':'halimaafrooz@gmail.com',
    'home':'sunzidahumaira.311@gmail.com'}
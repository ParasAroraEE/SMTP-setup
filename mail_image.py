import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('Gmail_User')
EMAIL_PASSWORD = os.environ.get('Gmail_Pass')
msg = EmailMessage()
msg['Subject'] = 'python msg with image'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'parasaroraee@gmail.com'
msg.set_content('image python mail')

with open('prs2.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

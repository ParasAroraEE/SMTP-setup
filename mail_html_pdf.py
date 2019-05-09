import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('Gmail_User')
EMAIL_PASSWORD = os.environ.get('Gmail_Pass')

contacts = ['parasaroraee@gmail.com', 'pawanab@gmail.com', 'deekshasachdeva30@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'python msg with html and image'
msg['From'] = EMAIL_ADDRESS
# msg['To'] = contacts
msg['To'] = 'parasaroraee@gmail.com'
msg.set_content('image python mail')
msg.add_alternative("""\
 <!DOCTYPE html>
 <html>
    <body>
        <h1 style="color:red;">This is an HTML Email!</h1>
    </body>
 </html>
    """, subtype='html')

files = ['prs1.jpg', 'prs2.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# files = ['resume.pdf']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name

#     msg.add_attachment(file_data, maintype='application', subtype='octet-strean', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

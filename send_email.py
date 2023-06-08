import smtplib
import ssl
import os
from email.message import EmailMessage

email_password = os.environ.get('EMAIL_PASSWORD')
# Set the sender and recipient email addresses
sender = 'your_email@email.com'
recipient = 'recipient_email@email.com'

# Set the subject and content of the email
subject = 'Hello'
content = 'Coding rocks!'

em = EmailMessage()
em['From'] = sender
em['To'] = recipient
em['Subject'] = subject
em.set_content(content)

# Secure sensitive data
context = ssl.create_default_context()

# Connet to the SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, email_password)
    smtp.sendmail(sender, recipient, em.as_string())




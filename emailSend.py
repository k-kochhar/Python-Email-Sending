import vault
import smtplib
from email.message import EmailMessage
import ssl
import emailContent

# Retrieving sending credentials
senderEmail = vault.senderEmail
senderPasscode = vault.senderPasscode
receiverEmail = vault.receiverEmail

subject = emailContent.subjectLine
body = emailContent.message

# Depositing email content
em = EmailMessage()
em['From'] = senderEmail
em['To'] = receiverEmail
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# Logging into and sending email through specified parameters
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
	smtp.login(senderEmail, senderPasscode)
	smtp.sendmail(senderEmail, receiverEmail, em.as_string())


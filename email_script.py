import smtplib
from email.message import EmailMessage

# with open('textfile.txt') as text:
# 	email = EmailMessage()
# 	email.set_content(text.read()) 

email = EmailMessage()
email['from'] = 'Spider'
email['to'] = 'aq.syed007@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content('I\'m a unhatched programmer!')


with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('example@mail.com', '***********************')
	smtp.send_message(email)
	print('Its done. alright my dear friend.')
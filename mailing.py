import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

config_file='configuration'

def send_mail(subject,body,reciever):
	

	with open(config_file) as fp:
		lines = fp.readlines()
	first_line_to_read = [i for i, line in enumerate(lines) if 'MAILING_DETAILS:' in line][0] + 1
	last_line_to_read = [i for i, line in enumerate(lines) if 'EOF' in line][0]
	
	for name in lines[first_line_to_read:last_line_to_read]:
		name=name.split(':')
		if name[0]=='SENDER_USERNAME':
			sender=name[1].split('\n')[0]
		elif name[0]=='SENDER_PASS':
			password=name[1].split('\n')[0]
	
	msg = MIMEMultipart()
	msg['From'] = sender
	msg['To'] = reciever
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))
	
	
	try:
		smtpObj = smtplib.SMTP('smtp.gmail.com:587')
		smtpObj.starttls()
		smtpObj.login(sender,password)
		smtpObj.sendmail(sender, reciever, msg.as_string())
	
	except smtplib.SMTPConnectError:
		msg='Mailing Error : error occured during connection with server.'
		
		
	except smtplib.SMTPAuthenticationError:
		msg='Mailing Error: Invalid username and/or password'
		
		
	except smtplib.socket.gaierror:
		msg='Mailing Error : Check Internet connection.'
		
	except Exception as e:
		msg='Mailing Error: Try again'

	else:
		msg="Admin has been successfully notified of the error via email."
		smtpObj.quit()

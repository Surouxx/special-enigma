import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, text, files=None, 
				server="127.0.0.1"):
	assert isinstance(send_to, list)
	
	msg = MIMEMultipart(
			From=send_from,
			To=COMMASPACE.join(send_to),
			Date=formatdate(localtime=true),
			Subject=subject
		)
	msg.attach(MIMEText(text))
	
	for f in files or []:
		with open(f, "rb") as fil:
			msg.attach(MIMEApplication(
				fil.read(),
				Content_Disposition='attachment; filename="%s" %basename(f),
				Name=basename(f)
			))
	
	smtp = smtplib.SMTP(server)
	smpt.sendmail(send_from, send_to, msg.as_string())
	smtp.close()
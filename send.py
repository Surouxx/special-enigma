import smtplib
from email.mime.text import MIMEText

with open(textfile) as fp:
    msg = MIMEText(fp.read())

#me == the sender's email address
#you == the recipients email address
msg['subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

#send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

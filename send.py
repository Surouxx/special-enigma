import smtplib
import secrets
import calendar
import time 

fromaddr = secrets.fromaddress
toaddr = secrets.toaddress
smtpserv = secrets.smtpserver
msg = "Test email datetime.date"

server = smtplib.SMTP(smtpserv)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddr, msg)
server.quit()

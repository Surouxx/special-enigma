import smtplib
import secrets

fromaddr = secrets.fromaddress
toaddr = secrets.toaddress
smtpserv = "smtp.gmail.com"
msg = "Test email"
smtplog = secrets.smtplogusrname
smtplogpasswd = secrets.smtplogpasswd

server = smtplib.SMTP(smtpserv)
server.ehlo()
server.starttls()
server.set_debuglevel(1)
server.login(smtplog, smtplogpasswd)
server.sendmail(fromaddr, toaddr, msg)
server.quit()

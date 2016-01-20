from smtplib import SMTP
import datetime
import secrets

debuglevel = 0

fromaddr = secrets.fromaddress
toaddr = secrets.toaddress
smtpserv = secrets.smtpserver
smtplog = secrets.smtplogusrname
smtppasswd = secrets.smtplogpasswd

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect(smtpserv, 26)
smtp.login(smtplog, smtppasswd)

from_addr = "Ian <seversonian@gilbertschool.org>"
to_addr = "surouxx@gmail.com"

subj = "TEST"
date = datetime.datetime.now().strftime("%d/%m/%y %h:%m")

message_text = "This is a test\nThis is a test\nThis is a test"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" %(from_addr, to_addr, 
subj, date,message_text)

smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()

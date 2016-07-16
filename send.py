import smtplib
import secrets
import sys

try:
    mail_from = str(sys.argv[1])
    mail_to = str(sys.argv[2])
    subject_line = str(sys.argv[3])
    msg_body = str(sys.argv[4])
except IndexError:
    print ("Error: Enter the from, to, subject, and msg body of the email to complete")

msg = "From: {} To: {} Subject: {} {}".format(mail_from, mail_to,
    subject_line, msg_body)
 
server = smtplib.SMTP_SSL(secret.server)
server.set_debuglevel(1)
server.login(secret.username, secret.password)
server.sendmail(secret.fromaddr, secret.toaddr, msg)
server.quit()


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

print(mail_from)
password = raw_input("Please type in your password to log into your email.\n")

msg = "From: {} To: {} Subject: {} {}".format(mail_from, mail_to,
    subject_line, msg_body)

server = 'smtp.gmail.com'

server = smtplib.SMTP_SSL(server)
server.set_debuglevel(1)
server.login(mail_from, password)
server.sendmail(mail_from, mail_to, msg)
server.quit()


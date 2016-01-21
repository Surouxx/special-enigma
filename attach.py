import smtplib 
import mimetypes 
import email
import email.mime.application
import secrets

msg = email.mime.Multipart.MIMEMultipart
msg['Subject'] = 'Greeting'
msg['From'] = secrets.smtplogusrname
msg['To'] = secrets.toaddress

body = email.mime.Text.MIMEText("""Do you want to play a game?\n (Y,n)""")
msg.attach(body)

filename = 'sample.pdf'
fp=open(smple.pdf, 'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
att.add_header('Content-Disposition','attachment,filename=%s'% filename)
msg.attach(att)

s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login(smtplogusrname, smtplogpasswd)
s.sendmail(smtplogusrname, [secrets.toaddress], msg.as_string())
s.quit()

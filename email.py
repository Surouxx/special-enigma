#This is a template, not the final file.

import smtplib
import base64

filename = "~/ian/testfile.txt"

#Read a file and encode it into base64 format.
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.base64encode(filecontent) # base64

sender = 'seversonian@gilbert.org'
reciever = 'madisong@gilbertschool.org'

marker = "AUNIQUEMARKER"

body = """
This is a test email to send an attachment
"""
#Defining the main headers.
part1 = """From: <seversonian@gilbertschool.org>
To: <madisong@gilbertschool.org>
Subject: Attachment Test
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

#Define the message action.
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body, marker)

#define the attachment section. 
part3 = """Content-Type: miltipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    smtpp0bj = smtblib.SMTP('localhost')
    smtpp0bj.sendmail(sender, reciever, message)
    print "Successfully Sent Email :)\n"
except Exception:
    print "Error: unable to send email :("

#!/usr/bin/python
import smtplib
def send_email(sender, receiver, message):
        smtpObj = smtplib.SMTP('smtp2010.searshc.com', 25)
        smtpObj.sendmail(sender, receiver, message)
        return True

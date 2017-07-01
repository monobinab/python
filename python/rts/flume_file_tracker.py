__author__ = 'msaha'
#!/usr/bin/python
import sys
import smtplib
from file_tracker import *
from datetime import date, timedelta, datetime

def send_email(sender, receiver, message):
        smtpObj = smtplib.SMTP('smtp2010.searshc.com', 25)
        smtpObj.sendmail(sender, receiver, message)
        return True

current_month = datetime.now().month
current_year = datetime.now().year
current_day = datetime.now().day
current_date = str(current_year) + "/" + str(current_month) +"/" + str(current_day)


parent_incoming_dir = "/incoming/rts/flume/jboss"
incoming_dir = parent_incoming_dir + "/" + current_date

print incoming_dir

message = """Subject: There may be a problem with flume files for Jboss Incoming \n
    Please check the flume incoming dir:""", incoming_dir
sender = "msaha@searshc.com"
receiver = "msaha@searshc.com"

new_cnt_file = "/staging/new_cnt.txt"
old_cnt_file = "/staging/old_cnt.txt"

new_cnt = open(new_cnt_file, 'r').readlines()
new_cnt = int(new_cnt[0].strip())

old_cnt = open(old_cnt_file, 'r').readlines()
old_cnt = int(old_cnt[0].strip())


if file_tracker(new_cnt, old_cnt):
    print "success"
else:
    print "email being sent"
    # send failure email
    send_email(sender, receiver, message)







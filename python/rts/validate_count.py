
import sys
import smtplib
sender = 'monobina.saha@searshc.com'
#receivers = ['monobina.saha@searshc.com', 'rtsteam@searshc.com']
receivers = ['monobina.saha@searshc.com']
message = ""

input_file='/staging/msaha/storm_cnt/000000_0'
input_file_handle=open(input_file, 'r')

minhour = ""
hrs = 0
maxhour = ""
member_cnt = ""
storm_count_list=[]
i=0

#for line in input_file_handle:
#    if line is not None:
#        try:
#            storm_count_list.insert(i, line.strip('\n'))
#            i = i + 1
#        except:
#            raise;


#print("counts are: ", storm_count_list)
#min_hour=storm_count_list[0]

for line in input_file_handle:
    if line is not None:
        fields=line.split(",")
        minhour=fields[0]
        hrs=fields[1]
        maxhour=fields[2]
        member_cnt=fields[3]

print(member_cnt)
print(hrs)
if int(member_cnt) < 100000 and int(hrs) < 24:
    print("will send email")
    message = """Subject: There may be a problem with yesterday's API_STORM_LOG hive table load\n
    This is to notify RTS team that yesterday's hadoop job to load storm table either didn't run or there was a problem:
    Number of distinct hours is """ + str(hrs) + " number of members loaded is " + str( member_cnt)
    try:
        smtpObj = smtplib.SMTP('smtp2010.searshc.com', 25)
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except:
        print("Error: unable to send email")
        #continue;





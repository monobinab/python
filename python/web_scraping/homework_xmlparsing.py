import urllib
import xml.etree.ElementTree as ET
sum_cnt = 0

url = raw_input('Enter URL:' )  # prompt for url
xml = urllib.urlopen(url).read()  # read the entire URL and store in this python object
commentinfo = ET.fromstring(xml)  #reads and parses the xml
lst = commentinfo.findall('comments/comment') # break the complex xml into a list
print 'Comment count:', len(lst)  #find length of list

#loop through the list and find the tag for count and get the value of it and store it in a variable
for item in lst:
    cnt = item.find('count').text #it has only text function as per my knowledge
    #print cnt
    cnt1 = int(cnt) #convert to integer so that we can sum it
    print cnt1
    sum_cnt = sum_cnt +cnt1  #it has to be saved in sum_cnt variable in both so that it keeps the previous sum_cnt and adds to it
    #break

print 'Sum of Count:', sum_cnt

#the structure of url content is below. part of it is pasted:

<commentinfo>
<note>
This file contains the actual data for your assignment - good luck!
</note>
<comments>
<comment>
<name>Derri</name>
<count>99</count>
</comment>
<comment>
<name>Wai</name>
<count>98</count>
</comment>
<comment>
<name>Aleena</name>
<count>98</count>
</comment>
</comments>
</commentinfo>
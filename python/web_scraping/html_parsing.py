#reading web page
import urllib
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print line.strip()
#write loop here to find any other link present and then go back to second line, put in fhand and open and read


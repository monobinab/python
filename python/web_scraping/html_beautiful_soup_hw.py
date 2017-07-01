import urllib
from BeautifulSoup import *

url=raw_input('Enter url: ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

table=soup.find("span", {"class": "comments"})
th = table.find('th', text="comments")
td = th.findNext('td')

#print tags.attrs
#tags1=soup.find(attrs={"name": "Comments"})
#print 'Tags1', tags1

print tags
print len(tags)
print td





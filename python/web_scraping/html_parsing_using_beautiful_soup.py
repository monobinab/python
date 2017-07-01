import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

print html
print soup
print "ending content"
#retrive a list of the anchor tags
#each tag is like a dictionary of HTML attributes
tags = soup('a')
print tags

for tag in tags:
    print tag.get('href', None) # this is the standard way to scraping by printing hrefs
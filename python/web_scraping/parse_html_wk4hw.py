import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
numlist = list()
num = 0
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('td')
for tag in tags:
    print tag.get('Comments', None)
   # Look at the parts of a tag
    print 'TAG:',tag
    #tag.strip()
    #stuff = re.findall('([0-9]+)', tag)
    #print stuff


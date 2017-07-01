import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()   # this will read the entire page
soup = BeautifulSoup(html)

#Retrieve a list of the anchor tags
# each tag is like a dictionary of HTML attributes

tags = soup('a') #give me all 'a' anchor tags only e.g. <a, href = ".....">
for tag in tags:
    print tag.get('hrf', None) #go through all the anchor tags and give all href, initial value is none


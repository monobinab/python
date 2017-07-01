#program to show how twitter augment works. We are going to read everything from this url. Oauth sends the signature back. Not actual secret stuff.

import urllib
from twurl import augment

print '* Calling Twitter....'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
    {'screen_name': 'drchuck', 'count': '2'})
print url
connection = urllib.urlopen(url) #OPEN URL
data = connection.read() #returns json of body here
print data
headers = connection.info().dict # returns json of header. Header is a dictionary
print headers


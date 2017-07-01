import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_168968.json'

print 'Retrieving url', url
uh = urllib.urlopen(url)
data = uh.read()
print 'retrieved data', len(data)
try:
    js = json.loads(str(data))
except:
    js = None

print json.dumps(js, indent =4)
sum_cnt = 0
for cnt in js['comments']:
    cnt = cnt['count']
    sum_cnt = cnt + sum_cnt
print sum_cnt  # it worked fine.


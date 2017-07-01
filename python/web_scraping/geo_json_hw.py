import urllib
import json

service_url = 'http://python-data.dr-chuck.net/geojson?'
address = raw_input('Enter Location: ')

url = service_url + urllib.urlencode({'sensor':'false',
                                         'address': address})
print 'Retrieving URL', url
uh = urllib.urlopen(url)
data = uh.read()

try:
    js = json.loads(str(data))
except:
    js = None

print 'Printing the json', json.dumps(js, indent = 4)
print 'Retrieved', len(data)

place_id = js["results"][0]["place_id"]
print place_id


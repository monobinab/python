import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #geocoding api url

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor':'false',
                                         'address': address})  #encode the address after the url. sensor and address are key value pairs in dictionary
    print 'Retrieving', url
    uh = urllib.urlopen(url) #url open
    data = uh.read()  #read the whole thing
    print 'Retrieved', len(data), 'characters'

    try: js = json.loads(str(data))  #js is the whole json
    except: js = None
    if 'status' not in js or js['status'] !='OK':  #if the exception happened or found ok
        print '====Failure to Retrieve'
        print data
        continue

    print json.dumps(js, indent=4) #dumpsis dump in string. js is the parsed dictionary

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat', lat, 'lng', lng
    location = js['results'][0]['formatted_address']
    print location

##########################################################
#what the above code will return
#Google Geocoding API
#http://maps.googleapis.com/maps/api/geocode/json?
#sensor=false&address=Ann+Arbor%2C+MI
USSJOML313761:web_scraping msaha$ python retrieve_data_from_google_geocoding_api.py
Enter location: san jose, ca
Retrieving http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=san+jose%2C+ca
Retrieved 1744 characters
{
    "status": "OK",
    "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                "bounds": {
                    "northeast": {
                        "lat": 37.4695381,
                        "lng": -121.589154
                    },
                    "southwest": {
                        "lat": 37.124493,
                        "lng": -122.0456679
                    }
                },
                "viewport": {
                    "northeast": {
                        "lat": 37.4695381,
                        "lng": -121.589154
                    },
                    "southwest": {
                        "lat": 37.124493,
                        "lng": -122.0456679
                    }
                },
                "location": {
                    "lat": 37.3382082,
                    "lng": -121.8863286
                }
            },
            "address_components": [
                {
                    "long_name": "San Jose",
                    "types": [
                        "locality",
                        "political"
                    ],
                    "short_name": "San Jose"
                },
                {
                    "long_name": "Santa Clara County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ],
                    "short_name": "Santa Clara County"
                },
                {
                    "long_name": "California",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ],
                    "short_name": "CA"
                },
                {
                    "long_name": "United States",
                    "types": [
                        "country",
                        "political"
                    ],
                    "short_name": "US"
                }
            ],
            "place_id": "ChIJ9T_5iuTKj4ARe3GfygqMnbk",
            "formatted_address": "San Jose, CA, USA",
            "types": [
                "locality",
                "political"
            ]
        }
    ]
}
lat 37.3382082 lng -121.8863286
San Jose, CA, USA
Enter location:
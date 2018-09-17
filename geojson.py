import urllib.request, urllib.parse, urllib.error
import json

base = "http://py4e-data.dr-chuck.net/geojson?"

user_input = input("Name of the University:\n")

if len(user_input) > 0:
	url = base + urllib.parse.urlencode({'address': user_input})
else :
	url = base

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
else :
	id = js["results"][0]["place_id"]
	print(id)
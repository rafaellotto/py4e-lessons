import urllib.request as req, urllib.parse, urllib.error
import re

url1 = "http://py4e-data.dr-chuck.net/comments_42.json"
url2 = "http://py4e-data.dr-chuck.net/comments_135226.json"

user_input = int(input("Which url? (1 for sample data or 2 for actual data)\n "))

if user_input == 1 :
	url = url1
else :
	url = url2

file = req.urlopen(url)
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
counts = list()

search = re.findall("\"count\":(\d+)", data.decode())

for item in search :
	counts.append(int(item))

print("Count",len(counts),"Sum",sum(counts))

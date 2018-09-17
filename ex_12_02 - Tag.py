import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = "http://py4e-data.dr-chuck.net/comments_42.html"
url2 = "http://py4e-data.dr-chuck.net/comments_135223.html"

user_input = int(input("Which url? (1 for sample data or 2 for actual data)\n "))

if user_input == 1 :
	url = url1
else :
	url = url2

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

counts = []
count = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
	# Look at the parts of a tag
	counts.append(int(tag.contents[0]))
	count += 1

sum = sum(counts)
print("Count:", count, "Sum:", sum)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sample = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

problem = "http://py4e-data.dr-chuck.net/known_by_Sheanne.html"

user_input = int(input('Enter 1 for sample or 2 for real problem: '))
count = None
position = int(input('Enter position: '))

while type(count) is not int :
    try :
        count = input('Number of repeats: ')
        count = int(count)
        count = abs(count)
        print("You want to repeat %d time(s) the position %d." % (count,position) )
    except ValueError:
        print("%s is not an integer.\n" % count)

if user_input == 1 :
    url = sample
else :
    url = problem

def spider(url) :
    urls = []
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        urls.append(tag.get('href', None))
    count -= 1
    print(count)

while count > 0 :
    spider(url)

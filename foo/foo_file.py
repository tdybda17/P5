import urllib.request as urlreq
import urllib.response
import urllib.error
import urllib.robotparser
import urllib.parse

from bs4 import BeautifulSoup

page_url = 'http://www.bloomberg.com/quote/SPX:IND'

page = urlreq.urlopen(page_url)

html = page.read()

soup = BeautifulSoup(html, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'logo'})

print(name_box.text.strip())

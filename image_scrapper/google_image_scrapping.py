import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen
from icrawler.builtin import GoogleImageCrawler
from image_scrapper.categories import categories

BATCH_SIZE = 2000
GOOGLE_IMAGE_SIZE = 'medium'

google_crawler = GoogleImageCrawler(storage={'root_dir': '/Volumes/BOOT/sports-car'}, downloader_threads=80, feeder_threads=20, parser_threads=20)
filter = dict(size=GOOGLE_IMAGE_SIZE)
google_crawler.crawl(keyword='sports car', filters=filter, max_num=BATCH_SIZE)


"""
for i in range(10):
    name_box = soup.find('img', attrs={'class': 'rg_ic rg_i'})
    print(name_box.src.strip())
"""
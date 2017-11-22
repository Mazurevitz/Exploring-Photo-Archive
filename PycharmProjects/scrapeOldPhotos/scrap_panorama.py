import urllib
import urllib.request
import requests
import re
import csv

from bs4 import BeautifulSoup


# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

data = []

for i in range(5):
    url = "https://panoramafirm.pl/oprogramowanie_komputerowe/%C5%9Bl%C4%85skie/firmy,{}.html".format(i)
    r = requests.get(url)
    print(url)
    soup = BeautifulSoup(r.content)
    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    data.extend(emails)

pure_mails = [em[7:] for em in data]
pure_mails = list(filter(None, pure_mails))
print(pure_mails)

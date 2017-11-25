import urllib
import urllib.request
import requests
import xlwt
from tempfile import TemporaryFile
from bs4 import BeautifulSoup


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')


# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

data = []

i=31
for i in range(40, 45):
    url = "https://panoramafirm.pl/oprogramowanie_komputerowe/%C5%9Bl%C4%85skie/firmy,{}.html".format(i)
    # url = "https://webcache.googleusercontent.com/search?q=cache:NR39_AkPKasJ:https://panoramafirm.pl/oprogramowanie_komputerowe/%25C5%259Bl%25C4%2585skie+&cd={}&hl=en&ct=clnk&gl=pl".format(i)
    r = requests.get(url)
    print(r.history)
    print(url)
    soup = BeautifulSoup(r.content)
    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    data.extend(emails)

pure_mails = [em[7:] for em in data]
pure_mails = list(filter(None, pure_mails))
print(pure_mails)

for i, e in enumerate(pure_mails):
    sheet1.write(i, 1, e)

name = "random.xls"
book.save(name)
book.save(TemporaryFile())

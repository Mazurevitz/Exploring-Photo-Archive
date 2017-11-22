import urllib
import urllib.request
from bs4 import BeautifulSoup


# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


soup = make_soup("https://audiovis.nac.gov.pl/obraz/5326/h:448/")

for img in soup.findAll("a", attrs={"opis":True}):
    print(img)
    # print(img.get('src'))

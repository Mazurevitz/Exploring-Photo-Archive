import urllib
import urllib.request
import re

from bs4 import BeautifulSoup


# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

source = "https://audiovis.nac.gov.pl/"

soup1 = make_soup(source + "haslo/190:1/")

i = 1   # numerator
for img in soup1.findAll("img"):
    print(img.get('src'))
    temp = img.get('src')

    filename = "woods" + str(i)
    print(filename)
    i += 1

    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

# soup_list = [make_soup("https://audiovis.nac.gov.pl/obraz/" + str(i) + "/h:448/") for i in range(10)]
# soup_list_filtered = [soup_list[i].findAll("a", attrs={"opis": True}) for i in range(len(soup_list))]
#
# for img in soup_list_filtered:
#     print(img)


# Check if value is integer
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

data = []
soup = make_soup("https://audiovis.nac.gov.pl/haslo/448:1/")
for img in soup.findAll("a", attrs={"href":True}):
    if represents_int(img.text):
        data.append(img.text)

last_site = max(data)


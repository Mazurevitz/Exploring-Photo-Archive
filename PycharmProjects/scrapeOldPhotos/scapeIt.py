import urllib
import urllib.request
import os.path
import pathlib

from bs4 import BeautifulSoup


# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


source = "https://audiovis.nac.gov.pl/haslo/"
save_path = "/home/wojciech/PycharmProjects/scrapeOldPhotos"


def get_pictures(category: str, name: str):
    """Args:
        category (str): "352:{}", where {} indicates page indexing
        name (str): name that will be given to each file
        """
    print("category: " + category + ", name: " + name)

    # print(os.path.dirname(name))
    # os.makedirs(os.path.dirname(save_path + name), exist_ok=True)

    img_num = 1  # file numerator
    for i in range(1, 2):
        soup1 = make_soup(source + category.format(i) + "/")
        for img in soup1.findAll("img"):
            print(img.get('src'))
            temp = img.get('src')

            filename = name + str(img_num)
            print(filename)
            img_num += 1

            pathlib.Path(os.path.join(save_path, name)).mkdir(parents=True, exist_ok=True)
            imagefile = open(os.path.join(save_path, name, filename)+".jpeg", 'wb')
            imagefile.write(urllib.request.urlopen(temp).read())
            imagefile.close()


# get_pictures("352:{}", "rivers")

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


# Find last page of given website
def find_last_page(category: str):
    data = []
    soup = make_soup(source + category.format(1) + "/")
    for img in soup.findAll("a", attrs={"href":True}):
        if represents_int(img.text):
            data.append(img.text)

    last_site = max(data)
    return last_site

print(find_last_page("352:{}"))

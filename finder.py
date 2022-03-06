from bs4 import BeautifulSoup
import requests
import re

# PAGE = 1
# &page={PAGE}

part = str(input("Podaj numer: "))
url = f"https://www.iparts.pl/znajdz/?idCar=&query={part}"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

div = doc.find(class_="katalog-lista row")
item = div.find(text=re.compile(part))

# items_l = items.split(' ')
#
# print(items_l)
print(item)

parent = item.find_parent(class_="produkt middle-12")



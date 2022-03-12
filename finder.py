from bs4 import BeautifulSoup
import requests
import re
from excloader import get_col_value


PARTS = get_col_value()


def find_parts():
    for part in PARTS:
        url = f"https://www.iparts.pl/znajdz/?idCar=&query={part}"

        info = requests.get(url).text

        doc = BeautifulSoup(info, "html.parser")

        div = doc.find(class_="katalog-lista row")
        item = div.find_all(text=re.compile(part))

        print(item)
        print("--------")


find_parts()



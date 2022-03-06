from bs4 import BeautifulSoup
import requests
import re

part = input("Podaj numer: ")

url = f"https://www.iparts.pl/znajdz/?idCar=&query={part}"
page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="number-pager")
print(page_text)
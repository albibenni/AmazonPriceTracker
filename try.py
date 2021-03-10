import tkinter as tk  # per la gui
import re
import requests
from bs4 import BeautifulSoup
# file per prendere l'app e text per text
from tkinter import filedialog, Text, simpledialog
import os  # per fare funzionare l'app

root = tk.Tk()  # dove attaccare ...

firstTurn = True

items = []
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
link = 'https://www.amazon.it/dp/B08C7KG5LP/?coliid=IXAPLKS4W7CDY&colid=2V4EU7SZ03PXR&psc=1&ref_=lv_ov_lig_dp_it'


class genItem:
    
    def __init__(self, title, price, link, priceTarget):
        self.price = price
        self.title = title
        self.link = link
        self.priceTarget = priceTarget


#array di prefissi per titolo      
prefTitle = [re.compile('productTitle*'), re.compile('title*'), re.compile('productTitle*')]

#array di prefissi per price nuovo
prefNewPrice = [re.compile('productTitle*'), re.compile('title*'), re.compile('productTitle*')]


def soupTitleFinder(soup):
    i = 0;
    # len(array) = length of an array in Python
    while (i < len(prefTitle)):
        title = soup.find(id = prefTitle[i])
        if title is None:
            i = i+1
        else:
            return title
    

#insert a basic item (non book)
def addGeneralLink(link):    
    # for soup lib to scrape the link
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #se ci sono tanti modelli posso usare un array di espressioni regolari per ciascun tipo
    
    #search title string
    title = soupTitleFinder(soup)
    
    print (title.get_text())

# add an entire list of items

def addListOfItems(domain, link):    
    elements = []
    pref = re.compile('itemName_*')
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    for el in soup.find_all(id = pref, href = True):
        elements.append("https://www.amazon." + domain + el['href'])

# addListOfItems("it", link)
addGeneralLink(link)


#TEST
# page = requests.get(link, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')
# #se ci sono tanti modelli posso usare un array di espressioni regolari per ciascun tipo

# #search title string
# title = soup.find(id = "productTitle")
# print(title)
import csv
import numpy
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=google%20pixel%207%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

text = requests.get(url)

soup = BeautifulSoup(text.content, 'html.parser')

print(soup.prettify())
import csv
import numpy
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_58d1821a-3668-4c6d-b7ac-394cd1872b22_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=25jx9fklr40000001670132532514'
htm = requests.get(url)
soup = BeautifulSoup(htm.content, 'html.parser')
texth = soup.find_all('div')
for pr in texth:
    price = pr.find(class_ ='_30jeq3 _1_WHN1')
    print(price)

    
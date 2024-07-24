
# scraper.py

import requests

import csv

from bs4 import BeautifulSoup



url = 'http://example.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')



print(soup.title.text)







with open('data.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(["Title"])

    writer.writerow([soup.title.text])
from bs4 import BeautifulSoup
import requests

links = []

for i in range(51):
    print("Page " + str(i))

    url="http://books.toscrape.com/catalogue/page-" + str(i) + ".html"

    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        h3s = soup.findAll('h3')
        for h3 in h3s:
            a = h3.find('a')
            link = a['href']
            links.append("http://books.toscrape.com/catalogue/" + link)

print(links)
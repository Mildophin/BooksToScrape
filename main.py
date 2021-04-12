from bs4 import BeautifulSoup
import requests
import os

""""
image_url

print(links)

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')

"""

links = []
"""
url="http://books.toscrape.com/"

pageaccueil = requests.get(url)
soup = BeautifulSoup(pageaccueil.text, features="html.parser")
listing= int(soup.find('li', {'class': 'current'}).string.strip()[10:])
"""

for i in range(1, 3):
    print("Page " + str(i))

    url = "http://books.toscrape.com/catalogue/page-" + str(i) + ".html"

    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        h3s = soup.findAll('h3')
        for h3 in h3s:
            a = h3.find('a')
            link = a['href']
            links.append("http://books.toscrape.com/catalogue/" + link)

for link in links:

    responsebook = requests.get(link)

    if responsebook.ok:
        soup = BeautifulSoup(responsebook.text, features="html.parser")
        category = soup.findAll('li')
        category = category[2].find('a').string
        title = soup.findAll('h1')
        title = title[0].string
        image_url = soup.find('div', {'class': 'item active'}).find('img')
        image_url = "http://books.toscrape.com/" + image_url['src'][6:]
        if not os.path.exists("Photos"):
            os.makedirs("Photos")
        path = os.path.dirname(__file__)
        filename = image_url.split('/')[-1]
        completefilename = path + "/Photos/" + filename
        r = requests.get(image_url, allow_redirects=True)
        open(completefilename, 'wb').write(r.content)

        if soup.find('div', {'class': 'product_main'}).find('p', {'class': 'star-rating One'}):
            rating = "One"
        elif soup.find('div', {'class': 'product_main'}).find('p', {'class': 'star-rating Two'}):
            rating = "Two"
        elif soup.find('div', {'class': 'product_main'}).find('p', {'class': 'star-rating Three'}):
            rating = "Three"
        elif soup.find('div', {'class': 'product_main'}).find('p', {'class': 'star-rating Four'}):
            rating = "Four"
        elif soup.find('div', {'class': 'product_main'}).find('p', {'class': 'star-rating Five'}):
            rating = "Five"
        else:
            print("Inconnu")
        description = soup.findAll('p')
        description = description[3].string
        tds = soup.findAll('td')
        upc = tds[0].string
        pet = "".join([x for x in tds[2].string if ord(x) < 128])
        pit = "".join([x for x in tds[3].string if ord(x) < 128])
        numberavailable = "".join(c for c in tds[5].string if c.isdigit())
    '1234566890'
    print(link, image_url, upc, pet, pit, numberavailable, category, title, rating, description)

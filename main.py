from bs4 import BeautifulSoup
import requests

""""
review_rating
image_url


ratingbloc = soup.find(class_="product_main")
if soup.find(class_="star-rating One") != "None":
    rating = "One"
elif soup.find(class_="star-rating Two") != "None":
    rating = "Two"
elif soup.find(class_="star-rating Three") != "None":
    rating = "Three"
elif soup.find(class_="star-rating Four") != "None":
    rating = "Four"


links = []

for i in range(10):
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

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')

"""

url="http://books.toscrape.com/catalogue/sharp-objects_997/index.html"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    category = soup.findAll('li')
    category = category[2].find('a').string
    title = soup.findAll('h1')
    title = title[0].string
    description = soup.findAll('p')
    description = description[3].string
    tds = soup.findAll('td')
    upc = tds[0].string
    pet = "".join([x for x in tds[2].string if ord(x) < 128])
    pit = "".join([x for x in tds[3].string if ord(x) < 128])
    numberavailable = "".join(c for c in tds[5].string if c.isdigit())
'1234566890'
print(url, upc, pet, pit, numberavailable, category, title, description)
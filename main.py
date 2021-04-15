from bs4 import BeautifulSoup
import requests
import csv
import os


def scrape():
    links = []
    dictionary_book = {}

    url = "http://books.toscrape.com/"

    pageaccueil = requests.get(url)
    soup = BeautifulSoup(pageaccueil.text, features="html.parser")
    listing = int(soup.find('li', {'class': 'current'}).string.strip()[10:])+1

    for i in range(1, listing):
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
            mybook = {
                "title": title,
                "category": category,
                "link": link,
                "rating": rating,
                "image_url": image_url,
                "upc": upc,
                "pet": pet,
                "pit": pit,
                "numberavailable": numberavailable,
                "description": description
            }
            if dictionary_book.get(category, None):
                dictionary_book[category].append(mybook)
            else:
                dictionary_book[category] = [mybook]
    return dictionary_book

def print_to_csv(file_name, list_book):
    if not os.path.exists("Categories"):
        os.makedirs("Categories")
    path = os.path.dirname(__file__)
    file_name = path + "/Categories/" + file_name
    with open(file_name, mode='w', encoding="utf-8") as csv_file:
        fieldnames = list_book[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,quotechar='"', quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for dict_data in list_book:
            writer.writerow(dict_data)

if __name__ == "__main__":
    dictionary_book = scrape()
    for cat, list_book in dictionary_book.items():
        print_to_csv(f"{cat}.csv", list_book)

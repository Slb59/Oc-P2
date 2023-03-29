import requests
from bs4 import BeautifulSoup
import csv
import re
import time

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
#urls = ['https://books.toscrape.com/catalogue/page-{}.html'.format(i) for i in range(1,51)]

def scrape_book(book_url):
    book_data = {}
    page = requests.get(book_url, timeout=20)
    soup = BeautifulSoup(page.content,  "html.parser")

    # books = soup.find_all("article",{"class":"product_pod"})

    regex = re.compile("star-rating (.*)")
    csvFile =   open('monFichier.csv',mode='w', encoding='utf8', newline='')

    try:
        writer = csv.writer(csvFile)
        writer.writerow(['url','title','price','UPC','Availability','Description', 'image','Price (excl. tax)','Price (incl. tax)','Price (incl. tax)'])
        # for book_data in books:
        book_data={}
        book_data['url'] = book_url
        book_data['Title'] = soup.find("h1").text
        book_data['Availability'] = soup.find("p", {"class":"instock availability"}).get_text().strip()
        book_data['Price'] = soup.find("p",{"class":"price_color"}).get_text()
        book_data['Categories'] =  soup.find_all("li")[2].get_text().strip()
        book_data['Star'] = soup.find('p', {'class': regex})['class'][-1]
        book_data['UPC'] = soup.find("td").text
        book_data['Src'] ="http://books.toscrape.com/"+ soup.find("img")['src'][5:].strip()
        book_data['Product Description'] = soup.find_all("p")[3].text
        book_data['Price (excl. tax)'] = soup.find_all("td")[2].text
        book_data['Price (incl. tax)'] = soup.find_all("td")[3].text
        print(book_data)
        writer.writerow([str(d) for d in book_data.values()])
    finally:
        csvFile.close()

def main():
    scrape_book(url)

if __name__ == '__main__':
    main()
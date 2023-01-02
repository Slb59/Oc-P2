import requests
import re
from bs4 import BeautifulSoup

from logs.logger import Logger
class ProductInfo:
    def __init__(self, upc, title, desc, cat):
        self.universal_product_code = upc
        self.title = title
        self.product_description = desc
        self.category = cat

class Product:
    """Description of a book product"""
    def __init__(self):
        self.page_url = 'http://books.toscrape.com/catalogue/the-death-of-humanity-and-the-case-for-life_932/index.html'
        self.session = requests.Session()
        self.html = self.session.get(self.page_url).content

        self.price_including_tax = 0
        self.price_excluding_tax = 0

        self.number_available = 0

        self.review_rating = 0
        self.image_url = ''

        self.info = ''  # a ProductInfo class

    def __str__(self):
        return '[' + self.info.category + '] ' + self.info.title + ': ' + self.info.product_description

    def load(self):
        logger = Logger()
        logger.debug('begin load: ' + self.page_url)

        root = BeautifulSoup(self.html, 'html.parser')

        # find description
        desc = root.find('div', id=re.compile('product_description'))

        if desc is not None:
            desc = desc.next_sibling.next_sibling.text
        else:
            desc = ''

        # find upc, title and category
        upc = root.find_all('td')[0].text
        title = root.find('h1').text
        category = root.find('a', href=re.compile('category/books/')).text

        self.info = ProductInfo(upc, title, desc, category)

        # find available
        get_nbavailable = root.find('p', class_='instock availability').text.strip()
        pos_start = len('In stock (')
        pos_end = len(' available)')
        self.number_available = int(get_nbavailable[pos_start:-pos_end])

        # find prices
        self.price_excluding_tax = float(root.find_all('td')[2].text[1:])
        self.price_including_tax = float(root.find_all('td')[3].text[1:])

        # find rating
        self.review_rating = root.find('p', class_='star-rating')['class'][1]

        # find url image
        list_rep = root.find('img')['src'].split('/')[2:]
        print(list_rep)
        print('/'.join(list_rep))

        t='http://books.toscrape.com/'













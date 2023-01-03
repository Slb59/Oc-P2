import re
import textwrap

from bs4 import BeautifulSoup

from logs import LOGGER


class BookInfo:
    def __init__(self, upc, title, desc, cat):
        self.universal_product_code = upc
        self.title = title
        self.product_description = desc
        self.category = cat


class Book:
    """ Description of a book """
    def __init__(self, url, session):

        self.site_url = 'http://books.toscrape.com/'
        self.page_url = url
        self.session = session
        self.html = self.session.get(self.page_url).content

        self.price_including_tax = 0
        self.price_excluding_tax = 0

        self.number_available = 0
        self.review_rating = 0

        self.image_url = ''

        self.info = ''  # a BookInfo class

    def __str__(self):
        return '[' + self.info.category + '] ' + self.info.title

    def __repr__(self):
        return '\n'.join([
            f'title: {self.info.title}',
            f'category: {self.info.category}',
            f'page: {self.page_url}',
            f'description: '
            f'{textwrap.fill(self.info.product_description, width=150)}',
            f'universal product code: {self.info.universal_product_code}',
            f'price (tax): {self.price_including_tax}',
            f'price (no tax): {self.price_excluding_tax}',
            f'number available: {self.number_available}',
            f'review rating: {self.review_rating}',
            f'image url: {self.image_url}'
        ])

    def load(self):

        LOGGER.debug('book load: ' + self.page_url)

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

        self.info = BookInfo(upc, title, desc, category)

        # find available
        get_nbavailable = root.find(
            'p',
            class_='instock availability').text.strip()
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
        self.image_url = self.site_url + '/'.join(list_rep)

from category import Category
from book import Book
from logs import LOGGER
from bs4 import BeautifulSoup


class CategoryLoader:
    """ generate a category whith a collection of books """
    def __init__(self, session, url):
        self.session = session
        self.page_url = url
        self.html = self.session.get(self.page_url).content
        self.main_url = 'http://books.toscrape.com/catalogue/'

    def load(self):

        LOGGER.debug('Category load')

        root = BeautifulSoup(self.html, 'html.parser')

        name = root.find('h1').text

        cat = Category(name)
        cat.url = self.page_url

        ol = root.find('ol')

        for li in ol.find_all('li'):
            book_url = li.find('a')['href'].split('/')[3:]
            book_url = self.main_url + '/'.join(book_url)

            book = Book(book_url, self.session)
            book.load()

            cat.add_book(book)

        return cat

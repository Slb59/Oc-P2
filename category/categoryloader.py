from category import Category
from book import Book

class CategoryLoader:
    """ generate a category whith a collection of books """
    def __init__(self, session):
        self.session = session

    def load(self):
        cat = Category('Philosophy')

        url = 'http://books.toscrape.com/catalogue/' \
              'the-death-of-humanity-and-the-case-for-life_932/' \
              'index.html'

        book = Book(url, self.session)
        book.load()

        cat.add_book(book)
        cat.add_book(book)

        return cat

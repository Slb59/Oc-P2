
from book import *
from category import *
from app import ArgParser, BooksToScrape

import requests

def test_book():
    url = 'http://books.toscrape.com/catalogue/' \
        'the-death-of-humanity-and-the-case-for-life_932/' \
        'index.html'
    session = requests.Session()

    book = Book(url, session)
    book.load()
    print(repr(book))
    csv_book = BookExporter(book)
    csv_book.to_csv('csv/product.csv')


def test_category():

    session = requests.Session()

    cat_loader = CategoryLoader(session)
    cat = cat_loader.load()

    print(repr(cat))
    print(cat)
    csv_cat = CategoryExporter(cat)
    csv_cat.to_csv('csv/' + cat.name + '.csv')


def main():
    args = ArgParser()
    parameters = args.read_parameters()
    app = BooksToScrape(parameters)
    app.exec()


if __name__ == '__main__':
    test_category()

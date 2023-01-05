from category import *
from app import *

import requests

def test_category():

    session = requests.Session()
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3'

    cat_loader = CategoryLoader(session, url)
    cat = cat_loader.load()

    print(repr(cat))
    print(cat)

    if cat is not None:
        csv_cat = CategoryExporter(cat)
        csv_cat.to_csv('csv/' + cat.category_name + '.csv')


def main():
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = BooksToScrape(the_parameters)
    # my_app.scrapping()
    print(my_app)


if __name__ == '__main__':
    main()

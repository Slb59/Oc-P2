from category import *
from app import *
from book import *

import requests
from logs import LOGGER

def test_category():

    session = requests.Session()
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3'

    cat_loader = CategoryLoader(session, url)
    cat = cat_loader.load()

    print(repr(cat))
    print(cat)

    if cat is not None:
        cat_exporter = CategoryExporter(cat)
        cat_exporter.to_csv('csv/' + cat.category_name + '.csv')

def test_book():
    session = requests.Session()
    url = 'http://books.toscrape.com/catalogue/the-bridge-to-consciousness-im-writing-the-bridge-between-science-and-our-old-and-new-beliefs_840/index.html'
    book_loader = BookLoader(url, session)
    a_book = book_loader.load()
    print(repr(a_book))
    book_exporter = BookExporter(a_book)
    file_name = 'csv/a_book.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        book_exporter.to_csv(f)


    img_url = 'http://books.toscrape.com/media/cache/2b/44/2b4404e00c242bf1b8263bdd99c07354.jpg'
    a_book = Book('Test', 'Test')
    a_book.image_url = img_url
    print(a_book)
    book_exporter = BookExporter(a_book)
    file_name = 'img/test.png'
    book_exporter.export_img(file_name)

def main():
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = BooksToScrape(the_parameters)
    test_book()
    # my_app.scrapping()
    # print(my_app)

if __name__ == '__main__':
    main()

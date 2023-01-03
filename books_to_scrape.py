from logs import Logger

from products import *
from app import ArgParser, BooksToScrape

def load_sophies_world():
    book = Product()
    book.load()
    print(repr(book))
    csv_book = ProductExporter(book)
    csv_book.to_csv('csv/product.csv')


def main():
    log = Logger()
    args = ArgParser(log)
    parameters = args.read_parameters()
    app = BooksToScrape(parameters, log)
    app.exec()

if __name__ == '__main__':
    main()

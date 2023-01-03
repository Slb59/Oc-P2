from logs import *
import products
from products import *


def test_logging():
    logger = Logger()
    logger.debug('Ceci est un message de log au niveau DEBUG')
    logger.info('Ceci est un message de log au niveau INFO')
    logger.warning('Ceci est un message de log au niveau WARNING')
    logger.error('Ceci est un message de log au niveau ERROR')
    logger.critical('Ceci est un message de log au niveau CRITICAL')


def load_sophies_world():
    book = Product()
    book.load()
    print(repr(book))
    csv_book = ProductExporter(book)
    csv_book.to_csv('csv/product.csv')


def main():
    pass

def version():
    print(products.__version__)


if __name__ == '__main__':
    version()

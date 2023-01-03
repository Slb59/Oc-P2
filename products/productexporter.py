import csv
from logs import *


class ProductExporter:
    """ Export a book in a csv file """
    def __init__(self, book):
        self.book = book

    def to_csv(self, file):
        logger = Logger()
        logger.debug('begin book_to_csv: ' + file)

        with open(file, 'w', newline='') as f:

            writer = csv.writer(f)

            writer.writerow([
                self.book.page_url,
                self.book.info.universal_product_code,
                self.book.info.title,
                self.book.price_including_tax,
                self.book.price_excluding_tax,
                self.book.number_available,
                self.book.info.product_description,
                self.book.info.category,
                self.book.review_rating,
                self.book.image_url
            ])

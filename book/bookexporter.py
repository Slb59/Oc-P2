import csv
import requests
import os
from logs import LOGGER


class BookExporter:
    """ Export a book in a csv file """
    def __init__(self, book):
        self.book = book

    def to_csv(self, file):

        LOGGER.debug('export ' + str(self.book))

        output = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        data = [
                self.book.page_url,
                self.book.universal_product_code,
                self.book.title,
                self.book.price_including_tax,
                self.book.price_excluding_tax,
                self.book.number_available,
                self.book.product_description,
                self.book.category,
                self.book.review_rating,
                self.book.image_url
        ]

        output.writerow([str(d).encode('utf-8').decode('utf-8') for d in data])

    def export_img(self, directory):

        LOGGER.debug(' Load image: ' + self.book.image_url)
        r = requests.get(self.book.image_url).content

        # create category directory if not exists
        category_dir = directory + '/' + self.book.category.replace(' ', '_')

        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        file_name = category_dir + '/test.png'

        with open(file_name, "wb+") as f:
            f.write(r)


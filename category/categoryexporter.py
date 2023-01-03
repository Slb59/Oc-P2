import csv
from logs import LOGGER
from book import *

class CategoryExporter:
    """ Export the collection of books of a category to a csv file """
    def __init__(self, category):
        self.category = category

    def to_csv(self, file):
        LOGGER.debug('Export to csv file')

        with open(file, 'w', newline='', encoding='utf-8') as f:

            output = csv.writer(f)

            output.writerow([
                'product_page_url',
                'universal_ product_code (upc)',
                'title',
                'price_including_tax',
                'price_excluding_tax',
                'number_available',
                'product_description',
                'category',
                'review_rating',
                'image_url'
            ])

            for a_book in self.category.books:
                book_to_csv = BookExporter(a_book)
                book_to_csv.to_csv(f)

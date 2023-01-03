import csv
from logs import LOGGER


class CategoryExporter:
    """ Export the collection of books of a category to a csv file """
    def __init__(self, category):
        self.category = category

    def to_csv(self, file):
        LOGGER.debug('Export to csv file')


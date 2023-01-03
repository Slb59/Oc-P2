import app
from logs import LOGGER

class BooksToScrape:
    """ manage the extractor of books.toscrape.com website """
    def __init__(self, parameters):
        self.version = app.__version__
        self.csv_directory = parameters.csv_directory
        self.img_directory = parameters.img_directory

        self.url = 'http://books.toscrape.com/'
        self.categories = []
        self.nb_books = 0

        LOGGER.debug('Initialisation de BooksToScrape')

    def exec(self):

        LOGGER.info("Fin de chargement des données Books To Scrape")

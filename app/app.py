import app


class BooksToScrape:
    """ manage the extractor of books.toscrape.com website """
    def __init__(self, parameters, log):
        self.version = app.__version__
        self.csv_directory = parameters.csv_directory
        self.img_directory = parameters.img_directory
        self.log = log


        self.url = 'http://books.toscrape.com/'
        self.categories = []
        self.nb_books = 0

        self.log.debug('Initialisation de BooksToScrape')

    def exec(self):

        self.log.info("Fin de chargement des données Books To Scrape")

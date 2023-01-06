import app
import requests
import os

from bs4 import BeautifulSoup
from logs import LOGGER

from category import *


class BooksToScrape:
    """ manage the extractor of books.toscrape.com website """
    def __init__(self, parameters):
        self.version = app.__version__
        self.csv_directory = parameters.csv_directory
        self.img_directory = parameters.img_directory
        self.check_directories()

        self.session = requests.Session()
        self.url = 'http://books.toscrape.com/'
        self.categories = []

        LOGGER.debug('Initialisation de BooksToScrape')

    def __str__(self):
        nb_books = 0
        for c in self.categories:
            nb_books += len(c.books)
        return f'Books To Scrape: {len(self.categories)} categories ' \
               f'and a total of {str(nb_books)} books'

    def check_directories(self):
        """ create the directories csv and img if not exists """
        if not os.path.exists(self.csv_directory):
            os.makedirs(self.csv_directory)
        if not os.path.exists(self.img_directory):
            os.makedirs(self.img_directory)

    def to_csv(self):
        for cat in self.categories:
            csv_cat = CategoryExporter(cat)
            csv_cat.to_csv(self.csv_directory + '/' + cat.category_name + '.csv')

    def get_categories_url(self):

        """ get all the category url in the welcome page """

        categories_url = []

        # read the list of categories
        html = self.session.get(self.url).content
        root = BeautifulSoup(html, 'html.parser')

        div = root.find('div', class_='side_categories')

        len_index = len('/index.html')

        for li in div.find_all('li'):
            url = li.find('a')['href'][:-len_index]
            cat_url = self.url + url
            categories_url.append(cat_url)

        # minus the first one : it's a link throw all the books
        return categories_url[1:]

    def export_img(self):
        pass

    def scrapping(self):

        """ the main scrapping program """

        LOGGER.info("Début de chargement des données Books To Scrape")

        for url in self.get_categories_url():
            cat_loader = CategoryLoader(self.session, url)
            cat = cat_loader.load()
            self.categories.append(cat)

        LOGGER.info("Exportation des données Books To Scrape")

        self.to_csv()

        LOGGER.info("Chargement des images Books To Scrape")

        self.export_img()

        LOGGER.info("Fin de chargement des données Books To Scrape")

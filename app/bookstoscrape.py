import app
import requests
import os
from datetime import datetime
from time import strftime
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
            cat_exporter = CategoryExporter(cat)
            cat_exporter.to_csv(self.csv_directory + '/' + cat.category_name + '.csv')

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

    def search_double_title(self):
        books_title_modify = []
        for cat in self.categories:
            for book in cat.books:
                books_title_modify.append(book.title[:40])
        print(books_title_modify)

        with open("logs/books_title.txt", "w") as f:
            f.write("\n".join(books_title_modify))
        doubles = set()
        for book_title in books_title_modify:
            if books_title_modify.count(book_title) > 1:
                doubles.add(book_title)
        print(doubles)
        for cat in self.categories:
            for book in cat.books:
                if book.title[:40] == 'The Star-Touched Queen':
                    print(book)

    def export_pictures(self):
        """ Export the pictures of all the category in the img_directory folder """
        for cat in self.categories:
            cat.export_pictures(self.img_directory)

    def scrapping(self):

        """ the main scrapping program """

        LOGGER.info("Début de chargement des données Books To Scrape")
        start_time = datetime.now()

        for url in self.get_categories_url():
            cat_loader = CategoryLoader(self.session, url)
            cat = cat_loader.load()
            self.categories.append(cat)

        execution_time = (datetime.now() - start_time).strftime("%M:%S")
        LOGGER.info(f"--- {execution_time}  ---")

        LOGGER.info("Exportation des données Books To Scrape")

        self.to_csv()

        LOGGER.info("Chargement des images Books To Scrape")
        start_time = datetime.now()

        self.export_pictures()
        execution_time = strftime("%M:%S", datetime.now() - start_time)
        LOGGER.info(f"--- {execution_time}  ---")

        LOGGER.info("Fin de chargement des données Books To Scrape")

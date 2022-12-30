from logs.logger import Logger


class Product:
    def __init__(self):
        self.product_page_url = ''
        self.universal_product_code = ''
        self.title = ''
        self.price_including_tax = 0
        self.price_excluding_tax = 0
        self.number_available = 0
        self.product_description = ''
        self.category = ''
        self.review_rating = 0
        self.image_url = ''

    def __str__(self):
        return '[' + self.category + '] ' + self.title + ': ' + self.product_description

    def load(self, url):
        logger = Logger()
        logger.debug('begin load: ' + url)

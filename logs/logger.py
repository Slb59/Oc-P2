import logging

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('OCP2')
        file_handler = logging.FileHandler("logs/logs.txt")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%d/%m/%Y %H:%M:%S")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
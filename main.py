from logs.logger import Logger

def test_logging():

    logger = Logger()
    logger.debug('Ceci est un message de log au niveau DEBUG')
    logger.info('Ceci est un message de log au niveau INFO')
    logger.warning('Ceci est un message de log au niveau WARNING')
    logger.error('Ceci est un message de log au niveau ERROR')
    logger.critical('Ceci est un message de log au niveau CRITICAL')

def main():
    pass

if __name__ == '__main__':
    test_logging()
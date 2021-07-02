import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.critical)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('addresBook.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
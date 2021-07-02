import logging

logger = logging.getLogger()
logger.setLevel(logging.critical)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('clinicManagement.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
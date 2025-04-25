import logging

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='logging_demo.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logging.debug('debug message')
logging.error('error message')
logging.exception('exception message')
logging.info('info message')
logging.warning('warning message')

import logging

from loggertest import get_logger
from logging_demo import logging_test2

logger = get_logger(__name__)

def do_some():
    logger.debug("debug message")
    logger.warning("warn message")
    do_some2()

def do_some2():
    logger.debug("debug message")
    logging_test2.do_some3()
    logger.critical("critical message")





from loggertest import get_logger

logger = get_logger(__name__)

def do_some3():
    logger.debug("debug message")
    logger.warning("warn message")
    do_some4()

def do_some4():
    logger.debug("debug message")


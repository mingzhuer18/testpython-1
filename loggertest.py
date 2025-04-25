# import os.path
import logging.config
# from logging_dir.logging_test1 import do_some


# def init_logging():
#     logging.config.fileConfig('./logging.conf')


def get_logger(name):
    logging.config.fileConfig('./logging.conf')
    # return logging.getLogger('filehaha1')
    print(name)
    return logging.getLogger(name)

# logging.config.fileConfig('./logging.conf')
# logger = logging.getLogger('file')
# logger.debug("debug message")
# logger.warning("warn message")
# do_some()



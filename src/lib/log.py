import logging
from lib import constants


def set_default_file_handler(logger, log_path):
    formatter = logging.Formatter(constants.log.Logger.DEFAULT_FORMAT)
    fh = logging.FileHandler(filename=log_path, mode=constants.file.Mode.WRITE)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

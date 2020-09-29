import logging
import os

loggers = {}


def log(level, message, path=''):
    """
        log to file and console
    :param level: log level
    :param message: message
    :param path: log path
    :return:
    """
    """
    Log to multiple locations if multipleLocs is True
    """
    if path != '':
        file_name = os.path.splitext(path)[0]
        if not loggers.get(path):
            loggers[path] = logging.getLogger(path)
            path = "log/%s.log" % path
            init_log(loggers[path], path)
        logger = loggers.get(path)
    else:
        if not loggers.get('general'):
            loggers['general'] = logging.getLogger("general")
            path = "log/general.log"
            init_log(loggers['general'], path)
        logger = loggers.get('general')

    if level == 'info':
        logger.info(message)

    if level == 'error':
        logger.error(message)

    if level == 'debug':
        logger.debug(message)

    if level == 'exception':
        logger.exception(message)

    if level == 'critical':
        logger.critical(message)


def init_log(logger, path):
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(path)
    formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

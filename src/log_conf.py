import logging.config


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance()


@singleton
class Logger:
    def __init__(self):
        logging.config.fileConfig("logging.conf")
        self.logr = logging.getLogger("root")

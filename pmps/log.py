#!/usr/bin/env python

import logging

class Logger(object):
    level = logging.INFO
    # _log_format = '%(asctime)s %(levelname)s: %(message)s'
    format = '%(relativeCreated)05d %(levelname)s: %(message)s'
    # _log_datefmt = '%H:%M:%S,uuu'
    datefmt = None

    def __init__(self):
        pass

    def set_log_level(self, level):
        if isinstance(level, int):
            self.level = getattr(logging, level.upper(), None)

    def configure(self):
        logging.basicConfig(level=self.level, format=self.format, datefmt=self.datefmt)

    def get(self):
        return logging


logger = Logger()

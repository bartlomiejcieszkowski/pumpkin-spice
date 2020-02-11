#!/usr/bin/env python

from pmps.main import PmpsMain
from pmps.log import logger
import getopt
import sys
from pathlib import Path

import json
import pprint
import logging

_global_cfg = {}
_default_config = Path.cwd() / "nutmeg.json"
_log_level = logging.INFO
# _log_format = '%(asctime)s %(levelname)s: %(message)s'
_log_format = '%(relativeCreated)05d %(levelname)s: %(message)s'
# _log_datefmt = '%H:%M:%S,uuu'
_log_datefmt = None
handlers_verbose = False


def usage():
    print("""pumpkin-spice [device] [task]
             -h --help - prints help
             -v --verbose - makes log more verbose
             --log={DEBUG|INFO|WARNING|ERROR|CRITICAL} - sets log level, defaults to INFO
          """)


def set_log_level(loglevel):
    global _log_level
    if not isinstance(loglevel, int):
        _log_level = logging.INFO
    else:
        _log_level = getattr(logging, loglevel.upper(), None)


def configure_logger():
    logging.basicConfig(level=_log_level, format=_log_format, datefmt=_log_datefmt)


def load_config(cfg, path, append=True):
    if not isinstance(path, Path):
        return False
    if not path.is_file():
        return False

    with path.open() as cfg_file:
        local_cfg = json.load(cfg_file)
        if not append:
            cfg.clear()
        cfg.update(local_cfg)


def main():
    global __main_class
    __main_class = PmpsMain()
    __main_class.run()

#!/usr/bin/env python

import getopt
import sys
from pathlib import Path

import logging

_default_config = Path.cwd() / "nutmeg.json"
_log_level = logging.INFO
#_log_format = '%(asctime)s %(levelname)s: %(message)s'
_log_format = '%(relativeCreated)05d %(levelname)s: %(message)s'
#_log_datefmt = '%H:%M:%S,uuu'
_log_datefmt = None
handlers_verbose = False

def usage():
    print("""pumpkin-spice [device] [task]
             -h --help - prints help
             -v --verbose - makes log more verbose
             --log={DEBUG|INFO|WARNING|ERROR|CRITICAL} - sets log level, defaults to INFO
          """)

def set_log_level(loglevel):
    _log_level = getattr(logging, loglevel.upper(), None)
    if not isInstance(level, int):
        _log_level = logging.INFO


def configure_logger():
    logging.basicConfig(level=_log_level, format=_log_format, datefmt=_log_datefmt)


def main():
    print(sys.argv[0])
    # parse args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose", "log="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-v", "--verbose"):
            _verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("--log"):
            set_log_level(a)
        else:
            usage()
            sys.exit(2)

    configure_logger()
    logging.info("yay")


if __name__ == "__main__":
    main()


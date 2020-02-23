#!/usr/bin/env python

import getopt
import sys
from pathlib import Path

from pmps.log import logger

import pprint
import json


_default_config = Path.cwd() / "pumpkin_sample.json"

class PmpsMain(object):
    def __init__(self):
        self.cfg = {}

    def load_config(self, path, append=True):
        if not isinstance(path, Path):
            return False
        if not path.is_file():
            return False

        with path.open() as cfg_file:
            local_cfg = json.load(cfg_file)
            if not append:
                self.cfg = local_cfg
            self.cfg.update(local_cfg)

    def run(self):
        self.init()
        input("Press Enter to continue...")

    def init(self):
        print(sys.argv[0])
        # parse args
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose", "log="])
        except getopt.GetoptError as err:
            print(err)
            self.usage()
            sys.exit(2)
        for o, a in opts:
            if o in ("-v", "--verbose"):
                _verbose = True
            elif o in ("-h", "--help"):
                self.usage()
                sys.exit(0)
            elif o in ("--log"):
                logger.set_log_level(a)
            else:
                self.usage()
                sys.exit(2)

        logger.configure()
        logger.get().info("yay")

        global _default_config

        logger.get().info(_default_config)
        self.load_config(_default_config)
        logger.get().info(pprint.pformat(self.cfg))

    def usage(self):
        print("""pmps [device] [task]
                 -h --help - prints help
                 -v --verbose - makes log more verbose
                 --log={DEBUG|INFO|WARNING|ERROR|CRITICAL} - sets log level, defaults to INFO
              """)

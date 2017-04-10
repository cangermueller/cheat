#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import os
import sys

import argparse
import logging

#  __dir = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, os.path.join(__dir, '../module'))


class App(object):

    def run(self, args):
        name = os.path.basename(args[0])
        parser = self.create_parser(name)
        opts = parser.parse_args(args[1:])
        return self.main(name, opts)

    def create_parser(self, name):
        p = argparse.ArgumentParser(
            prog=name,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='Description')
        p.add_argument(
            'in_file',
            help='Input file')
        p.add_argument(
            '-o', '--out_file',
            help='Output file')
        p.add_argument(
            '--verbose',
            help='More detailed log messages',
            action='store_true')
        p.add_argument(
            '--log_file',
            help='Write log messages to file')
        return p

    def main(self, name, opts):
        logging.basicConfig(filename=opts.log_file,
                            format='%(levelname)s (%(asctime)s): %(message)s')
        log = logging.getLogger(name)
        if opts.verbose:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        log.debug(opts)

        return 0


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)

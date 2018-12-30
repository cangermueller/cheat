#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import random
import sys

import argparse
import logging


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
      description='Example script.')
    p.add_argument(
      'in_dir',
      help='Input directory.')
    p.add_argument(
      '-o', '--out_dir',
      help='Output directory.')
    p.add_argument(
      '-t', '--test',
      action='store_true',
      help='Test without executing.')
    p.add_argument(
      '--seed',
      type=int,
      default=0,
      help='Seed of random number generator.')
    p.add_argument(
      '--verbose',
      action='store_true',
      help='More detailed log messages.')
    p.add_argument(
      '--log_file',
      help='Write log messages to file.')
    return p

  def main(self, name, opts):
    logging.basicConfig(filename=opts.log_file,
                        level=logging.DEBUG if opts.verbose else logging.INFO,
                        format='%(levelname)s (%(asctime)s): %(message)s')
    if opts.verbose:
      logging.debug(opts)

    if opts.seed is not None:
      random.seed(opts.seed)

    return 0


if __name__ == '__main__':
  app = App()
  app.run(sys.argv)

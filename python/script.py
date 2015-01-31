#!/usr/bin/env python

import argparse
import sys
import logging
import pdb
import os.path as path


if __name__ == '__main__':
    args = sys.argv
    name = path.basename(args[0])
    p = argparse.ArgumentParser(prog=name,
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                description='Description')
    p.add_argument('in_file', help='Input file', metavar='file')
    p.add_argument('-o', '--out_file', help='Output file')
    p.add_argument('-n', '--num', help='Number of repetitions.', default=10)
    p.add_argument('--verbose', help='More detailed log messages', action='store_true')
    p.add_argument('--log_file', help='Write log messages to file')
    opts = p.parse_args()

    logging.basicConfig(filename=opts.log_file,
                        format='%(levelname)s (%(asctime)s): %(message)s')
    log = logging.getLogger(name)
    if opts.verbose:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    log.debug(opts)


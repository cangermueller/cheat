#!/usr/bin/env python

import logging
import argparse

"""
output stream: stderr
"""


ap = argparse.ArgumentParser('Print content of file')
ap.add_argument('--log', help='Log level')
ap.add_argument('--log-file', help='Log filename')
opts = ap.parse_args()

if opts.log:
    level = getattr(logging, opts.log.upper(), None)
    if not isinstance(level, int):
        raise ValueError('Invalid log level %s' % opts.log)
else:
    level=logging.WARN

logging.basicConfig(level=level, filename=opts.log_file, format='%(levelname)s (%(asctime)s) - %(name)s: %(message)s')

logging.debug('Debug msg')
logging.info('Info msg')
logging.warn('Warn message')
logging.error('Error msg')
logging.critical('Critical message')

print()
log = logging.getLogger(__name__)
log.setLevel(logging.ERROR) # only for this logger, not logging
log.debug('Debug msg')
log.info('Info msg')
log.warn('Warn message')
log.error('Error msg')
log.critical('Critical message')


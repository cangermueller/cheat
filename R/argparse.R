#!/usr/bin/env Rscript

library(argparse)

p <- ArgumentParser(description='Description')
p$add_argument(
  'in_file',
  help='Input file')
p$add_argument(
  '-o', '--out_file',
  default='./out_file.h5',
  help='Output file')
p$add_argument(
  '--verbose',
  action='store_true',
  help='More detailed log messages')

args <- p$parse_args(commandArgs(TRUE))
print(args)

# is.null(opts$foo)   // TRUE if not given

#!/usr/bin/env Rscript

library(argparse)

p <- ArgumentParser(description='Description')
p$add_argument(
  'in_file',
  help='Input file')
p$add_argument(
  '-o',
  '--out_file',
  help='Output file')
p$add_argument(
  '--verbose',
  action='store_true',
  help='More detailed log messages',
  default=F)

args <- commandArgs(TRUE)
if (length(args) > 0) {
  opts <- p$parse_args(args)
} else {
  opts <- list()
}
if (opts$verbose) {
  print(opts)
}

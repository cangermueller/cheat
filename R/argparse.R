#!/usr/bin/env Rscript

library(argparse)

ap <- ArgumentParser(description='Concatenates several files')
ap$add_argument('files', metavar='FILE', nargs='+', help='Input files to be concatenated')
ap$add_argument('--output-file', dest='outfile', metavar='FILE', help='Output file')
ap$add_argument('--verbose', action='store_true', help='Be verbose')
ap$add_argument('--level', dtype='integer', default='100', help='Some number')

args <- ap$parse_args(commandArgs(TRUE))
print(args)

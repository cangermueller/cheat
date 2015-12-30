#!/usr/bin/env Rscript

library(argparse)
library(rmarkdown)
library(dplyr)
library(tools)

p <- ArgumentParser(description='Description')
p$add_argument(
  '--nrow',
  help='Number of rows',
  type='integer',
  default=10)
p$add_argument(
  '-o',
  '--out_file',
  default='output.pdf',
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
  opts$nrow <- 10
  opts$out_file <- 'output.pdf'
}

if (opts$verbose) {
  print(opts)
}

dat <- list()

dat$mat <- data.frame(a=rnorm(opts$nrow), b=runif(opts$nrow)) %>% tbl_df

rmd <- '/Users/angermue/tmp/R/script.Rmd'
out_format <- paste(file_ext(opts$out_file), 'document', sep='_')

rmarkdown::render(rmd, output_file=opts$out_file,
  output_format=out_format,
  output_dir=getwd())

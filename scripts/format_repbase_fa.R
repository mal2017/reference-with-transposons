#!/usr/bin/env Rscript

library(rtracklayer)
library(magrittr)
library(stringr)

args <- commandArgs(trailingOnly=TRUE)

fa <- rtracklayer::import(args[1])

nms <- names(fa) %>% str_extract(regex(".+(?=#)"))

nms %>% is.na %>% any %>% {!.} %>% stopifnot

names(fa) <- nms

rtracklayer::export(fa,args[2], format="fasta")

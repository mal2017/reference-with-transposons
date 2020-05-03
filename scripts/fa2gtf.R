#!/usr/bin/env Rscript

library(rtracklayer)
library(magrittr)
library(readr)
library(dplyr)

args <- commandArgs(trailingOnly=TRUE)

fai_tbl <- read_tsv(args[1], col_names = c("name","length","offset","a","b"))

gr_tbl <- fai_tbl %>%
  mutate(start=1, end = length, seqnames=name) %>%
  dplyr::select(seqnames, start, end)

# fill in transcript symbol and enough fields to make cellranger happy.
# feature type must be exon to be counted.
# https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/advanced/references
gr_tbl <- gr_tbl %>%
	  mutate(seqnames=as.character(seqnames)) %>%
	  mutate(gene_id = seqnames) %>%
	  mutate(gene_symbol = seqnames) %>%
	  mutate(transcript_symbol = seqnames) %>%
	  mutate(transcript_id = seqnames) %>%
	  mutate(type = "exon")

gr <- GRanges(gr_tbl)

# cellranger gets angry when strand != {+,-}
strand(gr[strand(gr) == "*"]) <- "+"

export(gr, args[2])

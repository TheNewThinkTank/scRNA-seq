if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("DESeq2")
BiocManager::install("GenomicDataCommons")

## Install libraries
install.packages("data.table")

## Load the libraries
library(data.table)
library(GenomicDataCommons)
library(DESeq2)

## Get the manifest
ge_manifest <- files() %>%
  filter( cases.project.project_id == 'TCGA-GBM') %>% 
  filter( type == 'gene_expression' ) %>%
  filter( analysis.workflow_type == 'STAR - Counts')  %>%
  manifest()

## Keep only the gene counts files - 174 patients available
ge_manifest <- ge_manifest[grep(pattern = "star_gene_counts", 
                                x = ge_manifest$filename), ]

## Download the first 20
fnames <- lapply(ge_manifest$id[1:20], gdcdata)

## Read the 1st file
asd <- fread(fnames[[1]][["6037d66c-5c66-4a9f-a255-ee76a354b86e"]], 
             data.table = F)
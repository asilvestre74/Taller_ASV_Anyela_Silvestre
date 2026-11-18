#!/usr/bin/env bash
# 03_phylogeny_iqtree.sh
# Multiple sequence alignment and Maximum-Likelihood phylogenetic inference (N = 45)
set -euo pipefail

mafft --auto data/acdS_45_secuencias_originales_NCBI.fasta > data/acdS_45_aligned_mafft.fasta
iqtree3 -s data/acdS_45_aligned_mafft.fasta -m MFP -bb 1000 -seed 402538 -nt AUTO -pre data/acdS_45_ML

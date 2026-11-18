#!/usr/bin/env python3
"""
01_fetch_ncbi_sequences.py
Retrieves canonical bacterial AcdS protein sequences from NCBI Entrez (E-utilities)
and computes exact amino acid lengths for Supplementary Table S1.
Author: Anyela Paola Silvestre Romero
"""
import urllib.request
import csv
import os

def fetch_sequences(accession_list, fasta_out):
    ids = ",".join(accession_list)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id={ids}&rettype=fasta&retmode=text"
    fasta_text = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
    with open(fasta_out, "w", encoding="utf-8") as out:
        out.write(fasta_text)
    print(f"Downloaded {fasta_text.count('>')} sequences to {fasta_out}")

if __name__ == "__main__":
    print("NCBI Entrez retrieval module ready.")

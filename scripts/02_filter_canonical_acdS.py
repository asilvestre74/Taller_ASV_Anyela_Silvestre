#!/usr/bin/env python3
"""
02_filter_canonical_acdS.py
Verifies canonical ACC deaminase diagnostic residues (Glu295 and Leu322, UW4 numbering)
to exclude D-cysteine desulfhydrase (dcyD) homologs.
Author: Anyela Paola Silvestre Romero
"""
CANONICAL_MOTIFS = ("E", "L")  # Diagnostic positions homologous to Glu295 and Leu322 in UW4

def validate_canonical_acdS(aligned_seq, pos_e295, pos_l322):
    res_e = aligned_seq[pos_e295]
    res_l = aligned_seq[pos_l322]
    return (res_e, res_l) == CANONICAL_MOTIFS

if __name__ == "__main__":
    print("Canonical acdS diagnostic filter ready.")

from Bio.Seq import Seq

with open("data/rosalind_prot.txt", "r") as rna_file:
    for rna in rna_file.readlines():
        seq_rna = Seq(rna)
        #Set the stop_synbol (default = *)
        print(seq_rna.translate(stop_symbol=""))


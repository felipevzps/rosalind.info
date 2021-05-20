from Bio.Seq import Seq
from Bio import SeqIO

introns = []
sequences_in_dna_file = 0
seq_count = 0

#Getting number of sequences in dna file
with open("data/rosalind_splc.txt", "r") as dna_file:
    for line in dna_file.readlines():
        if line.startswith(">"):
            sequences_in_dna_file += 1

#Getting DNA strand and introns
with open("data/rosalind_splc.txt", "r") as dna_file:
    records = list(SeqIO.parse(dna_file, "fasta"))
    #First string (0) is the DNA strand
    for i in range(1,sequences_in_dna_file):
        seq_count += 1
        dna = str(records[0].seq)
        introns.append(str(records[seq_count].seq))

#Removing introns from DNA strand
for intron in introns:
    if intron in dna:
       dna = dna.replace(intron, "")

#Translate DNA strand (DNA --> RNA --> PROTEIN)
seq = Seq(dna)
protein = seq.translate(stop_symbol="")
print(protein)

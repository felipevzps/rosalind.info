from Bio import SeqIO
from Bio.SeqUtils import GC

sequences = {}
for record in SeqIO.parse("data/rosalind_gc.txt", "fasta"):
    sequences[record.id] = GC(record.seq)

maxValue = max(sequences.values())
get_key = [key for (key, value) in sequences.items() if value == maxValue]

#Using '*' to remove the brackets from the list 
#and 'sep' to remove spaces of the start/end in the print
print(*get_key, "\n", maxValue, sep="")

from Bio import SeqIO
from Bio.SeqUtils import GC

sequences = {}
for record in SeqIO.parse("Bioinformatics Stronghold/teste.txt", "fasta"):
    sequences[record.id] = GC(record.seq)

maximo = max(sequences.values())
get_key = [key for (key, value) in sequences.items() if value == maximo]

# I am using * to remove the brackets from the list 
# and "sep" to remove spaces of the start/end in the print
print(*get_key,"\n",maximo, sep="")

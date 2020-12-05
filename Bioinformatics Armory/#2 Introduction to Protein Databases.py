from Bio import ExPASy
from Bio import SwissProt
import itertools 

with open("rosalind_dbpr.txt", "r") as sample:
    UniProt_ID = sample.read()
    UniProt_ID = UniProt_ID.rstrip()

handle = ExPASy.get_sprot_raw(UniProt_ID)
record = SwissProt.read(handle)
print(record.cross_references)
for i in record.cross_references:
    # Getting biological process (P) in the Gene Ontology (GO) tuple
    if "GO" in i and "P:" in i[2]:
        print(i[2].replace('P:', ''))
    


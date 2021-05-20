from Bio.Seq import Seq

with open("data/rosalind_ini.txt", "r") as sequence_file:
    sequence = Seq(sequence_file.read())

#Using count_overlap bcause python string's .count() is a non-overlapping count
#In some biological situations, overlapping count is necessary
print(sequence.count_overlap("A"), sequence.count_overlap("C"), sequence.count_overlap("G"), sequence.count_overlap("T"))

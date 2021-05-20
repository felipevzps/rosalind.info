file = open('data/rosalind_rna.txt', 'r')
string = file.read()

print(string.replace("T","U"))

file = open('data/rosalind_dna.txt', 'r')
DNAstring = file.read()

#using a function
def counter(n):
    baseSum = 0
    for i in DNAstring:
        if i == n:
            baseSum += 1
    return baseSum

print(counter('A'), counter('C'), counter('G'), counter('T'))

#pythonic way
print(DNAstring.coun('A'),DNAstring.coun('C'),DNAstring.coun('G'),DNAstring.coun('T'))
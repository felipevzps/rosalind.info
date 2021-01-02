file = open('/home/felipe/Documentos/vscode/Rosalind/rosalind_dna.txt', 'r')
DNAstring = file.read()

def counter(n):
    baseSum = 0
    for i in DNAstring:
        if i == n:
            baseSum += 1
    return baseSum

print(counter('a'), counter('c'), counter('g'), counter('t'))

file = open('data/rosalind_revc.txt', 'r')
string = file.read()

#input =  AAAACCCGGT
#output = TTTTGGGCCA -> ACCGGGTTTT (reverse complement of input)

#Checking ASCII table https://www.asciitable.xyz/
#A = 65
#T = 84
#C = 67
#G = 71

#Using translate 
table = {65:84, 84:65, 67:71, 71:67}
complement = string.translate(table)

print(complement[::-1])

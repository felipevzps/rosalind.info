arquivo = open('/home/felipe/Documentos/vscode/Rosalind/rosalind_revc.txt', 'r')
string = arquivo.read()

#fwd = AAAACCCGGT
#rvs_complement = TTTTGGGCCA -> ACCGGGTTTT

#Checking ASCII table https://www.asciitable.xyz/
#A = 65
#T = 84
#C = 67
#G = 71

table = {65:84, 84:65, 67:71, 71:67}
complement = string.translate(table)

print(complement[::-1])

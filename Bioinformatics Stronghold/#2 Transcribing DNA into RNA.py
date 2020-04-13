arquivo = open('/home/felipe/Documentos/vscode/Rosalind/rosalind_rna.txt', 'r')
string = arquivo.read()

print(string.replace("T","U"))

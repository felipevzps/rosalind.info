arquivo = open('/home/felipe/Documentos/vscode/Rosalind/rosalind_dna.txt', 'r')
string = arquivo.read()

def contador(n):
    contagem = 0
    for i in string:
        if i == n:
            contagem += 1
    return contagem

print(contador('a'), contador('c'), contador('g'), contador('t'))

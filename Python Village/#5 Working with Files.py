linhas=open('/home/felipe/Downloads/rosalind_ini5.txt','r')
ler_linhas=linhas.readlines()
i = 0
for line in ler_linhas:
    i += 1
    if (i%2) != 0:
        print(ler_linhas[i],end='') #end para remover os espaçamentos entre as linhas
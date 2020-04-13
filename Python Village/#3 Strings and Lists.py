texto=open('/home/felipe/Downloads/rosalind_ini3.txt','r')
#dividir as linhas em diferentes strings
dataset=texto.readlines()
#chamar a segunda string [1]
print(dataset[1])
#dividir números da lista (segunda linha)
numeros=dataset[1].split()
print(numeros)

#Precisa somar +1 no último número do slice pra pegar a palavra completa
d=int(numeros[0])
e=int(numeros[1])+1
f=int(numeros[2])
g=int(numeros[3])+1

print(dataset[0][d:e],dataset[0][f:g])
text=open('/home/felipe/Downloads/rosalind_ini3.txt','r')
#read lines
dataset=text.readlines()
#call second line [1]
print(dataset[1])
#split into 2 lines
numeros=dataset[1].split()
print(numeros)

#need to add +1 to get the complete word
d=int(numeros[0])
e=int(numeros[1])+1
f=int(numeros[2])
g=int(numeros[3])+1

print(dataset[0][d:e],dataset[0][f:g])
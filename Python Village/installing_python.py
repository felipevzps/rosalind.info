#1 - Installing Python
import this

#2 - Variables and Some Arithmetic
data=open('/home/felipe/Downloads/rosalind_ini2.txt','r',)
numbers=data.read()
splited=numbers.split()
print(splited)

a = int(splited[0])
b = int(splited[1])

print(a)
print(b)

#Pitágoras -> C²=A²+B²
c=b*b+a*a

print('O inteiro correspondente ao quadrado da hipotenusa do triângulo retângulo de AB é:',c)

#3 - Strings and Lists
#dataset="HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
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

print(d)
print(dataset[0][d:e],dataset[0][f:g])

#4 - Conditions and Loops
#criar números de a até b
#criar loop pra checar se número é impar
#armazenar primeiro impar em c
#somar próximo impar com c

dataset_impar=open('/home/felipe/Downloads/rosalind_ini4.txt','r')
dataset_numeros=dataset_impar.read()
dataset_numeros_inteiros=dataset_numeros.split()
print(dataset_numeros)

#Precisa somar +1 no último número do slice pelo mesmo motivo anterior
h=int(dataset_numeros_inteiros[0])
j=int(dataset_numeros_inteiros[1])+1

print(h,j)
sum = 0
for i in range(h,j):
    if (i%2) != 0:
        sum = sum +i
print(sum)

#5 - Working with Files
linhas=open('/home/felipe/Downloads/rosalind_ini5.txt','r')
ler_linhas=linhas.readlines()
i = 0
for line in ler_linhas:
    i += 1
    if (i%2) != 0:
        print(ler_linhas[i],end='') #end para remover os espaçamentos entre as linhas

#6 - Dictionaries


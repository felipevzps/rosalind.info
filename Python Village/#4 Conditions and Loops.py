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
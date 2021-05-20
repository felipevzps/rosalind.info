text=open('data/rosalind_ini3.txt','r')
dataset=text.readlines()
print(dataset[1])
num=dataset[1].split()
print(num)

#I had to add +1 to get the complete word
d=int(num[0])
e=int(num[1])+1
f=int(num[2])
g=int(num[3])+1

print(dataset[0][d:e],dataset[0][f:g])
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
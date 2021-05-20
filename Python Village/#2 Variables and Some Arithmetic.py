data=open('data/rosalind_ini2.txt','r',)
numbers=data.read()
splited=numbers.split()
print(splited)

a = int(splited[0])
b = int(splited[1])

print(a)
print(b)

#Pythagorean theorem -> C²=A²+B²
c=b*b+a*a

print('The integer corresponding to the square of the hypotenuse is:',c)
#create a to b numbers
#check if is odd
#storage first odd in c
#add next odd to c

dataset_odd=open('/home/felipe/Downloads/rosalind_ini4.txt','r')
dataset_numbers=dataset_odd.read()
dataset_numbers_integers=dataset_numbers.split()
print(dataset_numbers)

#need to add +1 to get the complete word
h=int(dataset_numbers_integers[0])
j=int(dataset_numbers_integers[1])+1

print(h,j)
sum = 0
for i in range(h,j):
    if (i%2) != 0:
        sum = sum +i
print(sum)
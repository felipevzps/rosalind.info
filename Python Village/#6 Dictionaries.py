text=open('data/rosalind_ini6.txt','r')

ocurrence = {}
data = []

#Split words
for i in text:
    data = i.split()

#Count word ocurrence
for word in data:
    ocurrence[word] = ocurrence.get(word, 0) + 1   
#print(ocurrences)

#Print solution requested format
for k,v in ocurrence.items():
    print(k, v)
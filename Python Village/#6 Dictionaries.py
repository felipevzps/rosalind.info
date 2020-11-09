text=open('Python Village/rosalind_ini6.txt','r')

ocurrences = {}
data = []

#Split words
for i in text:
    data = i.split()
#print(data)

#Count words ocurrences
for word in data:
    ocurrences[word] = ocurrences.get(word, 0) + 1   
#print(ocurrences)

#Print solution requested format
for k,v in ocurrences.items():
    print(k, v)
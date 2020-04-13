string = 'ACACACTGACTGACTGGTCAGTACCCCGTACGTAC'

counter = [0,0,0,0]

for n in range(0,len(string)):
    if string[n] == 'A':
        counter[0] += 1
    elif string[n] == 'C':
        counter[1] += 1
    elif string[n] == 'G':
        counter[2] += 1
    elif string[n] == 'T':
        counter[3] += 1

result = str(counter[0])+ ' ' + str(counter[1]) + ' ' + str(counter[2]) + ' ' + str(counter[3])

print(result)

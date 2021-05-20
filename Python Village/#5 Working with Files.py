lines=open('data/rosalind_ini5.txt','r')
read_lines=lines.readlines()
i = 0
for line in read_lines:
    i += 1
    if (i%2) != 0:
        print(read_lines[i],end='') #end = remove spaces 
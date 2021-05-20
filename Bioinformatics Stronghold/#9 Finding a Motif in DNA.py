with open("data/rosalind_subs.txt", "r") as string:
        #Assign 2 variables in the same time (line 1 (s) and line 2 (t))
        s,t = string.readlines()
        s = s.rstrip()
        t = t.rstrip()
 
position = []
#Determine the limit of the last slice 
max_pos = len(s) - len(t) + 1

for i in range(0, max_pos):
    #Slice and get only "t" matching
    if s[i:i+len(t)] == t:
        #The output needs to be i+1, so this line is necessary 
        position.append(str(i+1))

#Printing output without brackets
print(" ".join(position))


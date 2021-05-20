counter = -1
diff = 0
seq_list = []

with open("data/rosalind_hamm.txt", "r") as sequences:
    #read sequences from the file and split lines without '\n'
    for seq in sequences.read().splitlines():
        seq_list.append(seq)

a = seq_list[0]
b = seq_list[1]

for i in range(len(a)):
    counter += 1
    if a[counter] != b[counter]:
        diff += 1

print(diff)

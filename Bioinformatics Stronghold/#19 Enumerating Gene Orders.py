import itertools

with open("data/rosalind_perm.txt", "r") as sample:
    sample_input = sample.readlines()
    #Using join to get number in list and "int" to turn the number into integer
    #I also had to add 1 to the number, bcause the starting point to count is 0
    sample_int = int("".join(sample_input)) + 1
    sample_list = []

for i in range(1,sample_int):
    sample_list.append(i)

#Getting permutations 
permutation = list(itertools.permutations(sample_list))

print(len(permutation))
for item in permutation:
    print(*item)

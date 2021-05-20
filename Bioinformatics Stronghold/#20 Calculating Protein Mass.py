from collections import defaultdict

mass_content = dict()

#Creating monoisotopic mass dictionary
with open("data/monoisotopic_mass_table.txt") as monoisotopic_mass_dict:
    '''
    The monoisotopic mass table for amino acids is a 
    table listing the mass of each possible amino acid 
    residue, where the value of the mass used is the 
    monoisotopic mass of each residue:

    A   71.03711
    C   103.00919
    D   115.02694
    E   129.04259
    F   147.06841
    G   57.02146
    H   137.05891
    I   113.08406
    K   128.09496
    L   113.08406
    M   131.04049
    N   114.04293
    P   97.05276
    Q   128.05858
    R   156.10111
    S   87.03203
    T   101.04768
    V   99.06841
    W   186.07931
    Y   163.06333 
    '''
    for line in monoisotopic_mass_dict:
        mass_content[line.split()[0]] = float(line.split()[1])

count_mass = 0
#Opening sequence file and calculating the protein mass
with open("data/rosalind_prtm.txt", "r") as sampleInput:
    string = sampleInput.read().strip()
    for i in string:
        if i in mass_content.keys():
        #Getting i.values()
            count_mass += mass_content.get(i)

print(count_mass)

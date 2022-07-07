#Counting DNA Nucleotides
'''
Problem:
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
Sample Dataset:AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output:20 12 17 21
'''
#num1

data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
A_count = data.count('A')
C_count = data.count('C')
G_count = data.count('G')
T_count = data.count('T')
print(A_count,C_count,G_count,T_count)

#num2
'''
data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
A_count = C_count = G_count = T_count = 0
for i in data:
    if i == 'A':
        A_count += 1
    elif i == 'C':
        C_count += 1
    elif i == 'G':
        G_count += 1
    elif i == 'T':
        T_count += 1
print(A_count,C_count,G_count,T_count)
'''
#num3
'''
def dna(path):
    with open(path) as fp:
        seq = fp.readline()
    return count_nt(seq)
def count_nt(seq):
    table = {x:0 for x in 'ACGT'}   #创建字典table = {A:0,C:0,G:0,T:0}
    for i in seq:
        table[i] += 1  #碱基键的值+1
    return [b for a,b in table.items()]
print(dna(r'pyhton\rosalind\01.txt'))   #r''表示后面紧跟着的字符为原始字符，不进行转义
'''
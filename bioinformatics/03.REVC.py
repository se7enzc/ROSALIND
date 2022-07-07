''''
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string  is the string  formed by reversing the symbols of , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string  of length at most 1000 bp.

Return: The reverse complement  of .

data:AAAACCCGGT
output:ACCGGGTTTT
'''

data = 'AAAACCCGGT' #原始DNA序列

data_com = ''   #新建一个空白字符串

def change(seq):
    if seq == 'A':
        return 'T'
    elif seq == 'C':
        return 'G'
    elif seq == 'G':
        return 'C'
    elif seq == 'T':
        return 'A'

for i in data:
    change_seq = change(i)
    data_com += change_seq

data_com_rev = data_com[::-1]

print(data_com_rev)

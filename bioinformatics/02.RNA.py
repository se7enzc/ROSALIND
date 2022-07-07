'''
Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string corresponding to a coding strand, its transcribed RNA string is formed by replacing all occurrences of 'T' in with 'U' in .

Given: A DNA string having length at most 1000 nt.

Return: The transcribed RNA string of .

DATA : GATGGAACTTGACTACGTAAATT
output : GAUGGAACUUGACUACGUAAAUU
'''

DNA_data = 'GATGGAACTTGACTACGTAAATT'
RNA_data = DNA_data.replace('T','U')
print(RNA_data)


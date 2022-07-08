#Genome Assembly as Shortest Superstring
'''
For a collection of strings, a larger string containing every one of the smaller strings 
as a substring is called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves 
as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, 
in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: 
there exists a unique way to reconstruct the entire chromosome from these reads 
by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings 
(thus corresponding to a reconstructed chromosome).

题目大意是给定几条序列，任意序列一定会与另一条序列有overlap，且重叠区域至少占一半以上，这两条序列合并形成一条新的序列
这两条序列都能比对到这条新序列上，问最后合成到的最短的序列是什么
'''
file_input = open('input.txt','r')
all_sequence_list = file_input.read().splitlines()  #逐行读取txt，并生成列表
sequence_dict = {}
for i in range(0,len(all_sequence_list),2):
    sequence_dict[all_sequence_list[i]] = all_sequence_list[(i+1)]
print(sequence_dict)
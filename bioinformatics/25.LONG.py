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
seq_list = []
for i in range(0, len(all_sequence_list), 2):
    sequence_dict[all_sequence_list[i]] = all_sequence_list[(i+1)]
    seq_list.append(all_sequence_list[(i+1)])
print(sequence_dict)
print(seq_list)

# 参考从头组装的k_mer算法


def k_mer(seq):
    k_mer_list = []
    for i in range(len(seq)-2):
        # 从题目来看，序列长度为10bp，且k值必须为奇数，这里k值取的是3，单题目而言，取偶数也行
        k_mer_list.append(seq[i:i+3])
    return k_mer_list


def del_overlap(seq_1, seq_2):
    seq_1_k_mer_list = k_mer(seq_1)
    seq_2_k_mer_list = k_mer(seq_2)
    del_overlap_seq_list = []
    for i in range(len(seq_1_k_mer_list)-1, 0, -1):
        if seq_1_k_mer_list[-i:] == seq_2_k_mer_list[:i]:
            del_overlap_seq_list.append(seq_1 + seq_2[i+2:])
        elif seq_2_k_mer_list[-i:] == seq_1_k_mer_list[:i]:
            del_overlap_seq_list.append(seq_2 + seq_1[i+2:])
        else:
            del_overlap_seq_list.append(seq_1 + seq_2)
            del_overlap_seq_list.append(seq_2 + seq_1)
    return min(del_overlap_seq_list, key=len)
# print(del_overlap(seq1,seq2))


# 只能用一种相对无脑的方式破解了，已知只有4条reads，然后遍历所有组合
seq_assembly = []
for i in range(len(seq_list)-1):
    seq_1 = seq_list[i]
    seq_list_copy = seq_list.copy()  # 构建一个除去当前序列列表的副本
    seq_list_copy.remove(seq_1)
    #print(seq_list_copy)
    for ii in range(i+1, len(seq_list)):
        seq_2 = seq_list[ii]
        seq_contig_1 = del_overlap(seq_1, seq_2)
        seq_list_copy_2 = seq_list_copy.copy()
        seq_list_copy_2.remove(seq_2)
        seq_3 = seq_list_copy_2[0]
        seq_4 = seq_list_copy_2[1]
        seq_contig_2 = del_overlap(seq_3, seq_4)
        seq_assembly.append(del_overlap(seq_contig_1, seq_contig_2))
print(min(seq_assembly, key=len))

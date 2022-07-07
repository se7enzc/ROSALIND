'''
Finding a Most Likely Common Ancestor

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

大意是给几个同源序列,得到可能的原始序列,具体详情见原文

'''
#一看题干，应该是用矩阵运算（我不会）的方法会更快，但先尝试用新手方法

file_input = open('input.txt','r')
all_sequence_list = file_input.read().splitlines()  #逐行读取txt，并生成列表
sequence_list = []
for i in range(0,len(all_sequence_list)):
    if (i+1) % 2 == 0:
        sequence_list.append(all_sequence_list[i])
#print(sequence_list)

#获取一段序列中出现次数最多的碱基
def ancestor(data):
    A_count = data.count('A')
    C_count = data.count('C')
    G_count = data.count('G')
    T_count = data.count('T')
    ACGT_count =[A_count , C_count , G_count , T_count]
    ACGT = ['A','C','G','T']
    for i in range(len(ACGT_count)):
        if ACGT_count[i] == max(ACGT_count):
            ancestor_base = ACGT[i]
    return ancestor_base


def count(sequence):
    seq_count = len(sequence)
    seq_len = len(sequence[1])
    ancestor_seq = ''
    A_count = 'A: '
    C_count = 'C: '
    G_count = 'G: '
    T_count = 'T: '
    for i in range(0,seq_len):
        base_list = ''
        for o in range(0,seq_count):
            base_list += (sequence[o][i])
        #print(base_list)
        count_A = base_list.count('A')
        count_C = base_list.count('C')
        count_G = base_list.count('G')
        count_T = base_list.count('T')
        A_count += str(count_A) + ' '
        C_count += str(count_C) + ' '
        G_count += str(count_G) + ' '
        T_count += str(count_T) + ' '
        ancestor_base = ancestor(base_list)
        ancestor_seq += ancestor_base
    print(ancestor_seq,A_count,C_count,G_count,T_count,sep='\n')

count(sequence_list)
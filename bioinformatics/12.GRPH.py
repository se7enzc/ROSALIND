'''
Overlap Graphs
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
这个题目理解起来有点费劲，大意可能是在给定的几个序列中，任意一条序列的后3个碱基与其余一条序列的前3个碱基一致即可相连
是不是有点De novo测序的味道了
'''
#获取序列
file_input = open('input.txt','r')
all_sequence_list = file_input.read().splitlines()
sequence_list = {}
for i in range(0,len(all_sequence_list),2):
    sequence_list[all_sequence_list[i][1:]] = all_sequence_list[i+1]
#print(sequence_list)

#采用最简单的两两比对
for key1,value1 in sequence_list.items():
    sequence_list_2 = sequence_list.copy()  #获取第二条序列，先复制原字典，再删除已经拿来比较的第一条序列
    del sequence_list_2[key1]
    for key2,value2 in sequence_list_2.items():
        if value1[-3:] == value2[:3]:
            print(key1 + ' ' + key2)
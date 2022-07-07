#统计GC含量最高的一条序列

#处理每条序列，得到一个GC含量值
def GC_counts(dict):
    for key,value in dict.items():
        gc_count = (value.count('G') + value.count('C')) / len(value)
        gc_dict = {}
        gc_dict[key] = gc_count * 100
    return gc_dict

#获取GC含量值最高的那条序列
def GC_max(dict):
    value_max = max(dict.values())
    for key,value in dict.items():
        if value == value_max:
            return key


with open('/Users/bgi/python/Rosalind/rosalind.fasta') as file_test:
    list1 = file_test.read().splitlines()
    dict1= {}
    for i in range(int(len(list1)/2)):
        seq_title = list1[i*2][1:]
        dict1[seq_title] = list1[i*2+1]

gc_dict = GC_counts(dict1)
print(GC_max(gc_dict))  #打印GC含量最高的那条序列名称
print(gc_dict[GC_max(gc_dict)]) #打印对应的GC含量值

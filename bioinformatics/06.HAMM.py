'''
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
'''
#对比参考基因组，统计目标序列的点突变

def count_mut(conf,targ):
    count = 0
    for a,b in zip(conf,targ):
        if a != b:
            count += 1
    return count

with open('/Users/bgi/python/Rosalind/rosalind.fasta') as file_test:
    list1 = file_test.read().splitlines()
    seq_conf = list(list1[0])
    seq_targ = list(list1[1])
    print(count_mut(seq_conf,seq_targ))
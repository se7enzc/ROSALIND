#Locating Restriction Sites
'''
回文序列：正向序列与反向互补的序列相同
获取以下序列中的长度为 4-12 bp的回文序列
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
'''

#反向互补
def com(seq):
    seq_1 = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
    return seq_1.upper()[::-1]

def palin(seq):
    for x in range(len(seq)-3):
        for y in range(4,13):
            if x+y <= len(seq):   #获取字符串的右坐标最大不能超过长度值
                split_seq = seq[x:x+y]
                if split_seq == com(split_seq):
                    print(x+1,y,split_seq)

seq = 'TCAATGCATGCGGGTCTATATGCAT'
palin(seq)
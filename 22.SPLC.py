#RNA Splicing
'''
>Rosalind_10    #DNA序列
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA  #指定内含子序列
>Rosalind_15
ATCGGTCGAGCGTGT #内含子序列

剪切后的DNA翻译成氨基酸:MVYIADKQHVASREAYGHMFKVCA
根据基因组实际情况来看,单个内含子的序列唯一且只会在DNA中出现一次
ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG
'''
condon_dict = {
'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
'UAC':'Y', 'UAU':'Y', 'UAA':' ', 'UAG':' ',
'UGC':'C', 'UGU':'C', 'UGA':' ', 'UGG':'W',
}

dna_seq = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
intron_1 = 'ATCGGTCGAA'
intron_2 = 'ATCGGTCGAGCGTGT'

def trans(rna):
    condon_seq = ''
    for n in range(0,len(rna),3):   #遍历给定的序列，3个为一组
        if rna[n:n+3] in condon_dict.keys():
            condon_seq += condon_dict[rna[n:n+3]]
    return condon_seq

def splice(seq,intron):
    splice_seq = [seq]
    for i in range(len(intron)):    #默认内含子的按顺序在DNA中出现
        if splice_seq[i].find(intron[i]) != -1:
            mid_seq = splice_seq[i]
            del splice_seq[i]
            s = mid_seq.find(intron[i])
            splice_seq.append(mid_seq[:s])
            splice_seq.append(mid_seq[s+len(intron[i]):])
    spliced_dna = ''
    for i in splice_seq:
        spliced_dna += i
    return spliced_dna

intron =[intron_1,intron_2]
spliced_dna = splice(dna_seq,intron)
m_rna = spliced_dna.replace('T','U')
print(trans(m_rna))

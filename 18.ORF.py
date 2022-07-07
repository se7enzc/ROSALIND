#Open Reading Frames
'''
input:
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

output:
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
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

def com(seq):
    seq_1 = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
    return seq_1.upper()

def trans(rna):
    condon_seq = ''
    for n in range(0,len(rna),3):   #遍历给定的序列，3个为一组
        if rna[n:n+3] in condon_dict.keys():
            condon_seq += condon_dict[rna[n:n+3]]
    return condon_seq

def find_orf(seq):
    orf_list =[]
    for x in range(3):  #切记：不一定从第一个碱基开始翻译
        seq_1 = seq[x:]
        for i in range(0,int(len(seq_1)),3):
            if seq_1[i:i+3] == 'AUG':
                for a in range(i+3,int(len(seq_1)),3):
                    if seq_1[a:a+3] in ['UAA','UAG','UGA']:
                        orf_rna = seq_1[i:a]
                        orf_list.append(trans(orf_rna))
                        break
    return orf_list

dna_seq = open('input.txt','r').read().splitlines()[1]
rna_seq = dna_seq.replace('T','U')

#获取反向互补的序列
rev_dna_seq = dna_seq[::-1]     #倒序排列
com_rev_dna_seq = com(rev_dna_seq)
com_rev_rna_seq = com_rev_dna_seq.replace('T','U')

print(set(find_orf(rna_seq) + find_orf(com_rev_rna_seq)))   #用set去重



'''
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
将一段RNA序列翻译成氨基酸序列
Sample Dataset:AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output:MAMAPRTEINSTRING
'''
#先列一个密码字典，每一个密码子对应一个氨基酸
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

rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
dna = 'AGCCAUGUAGCUAACUCAGGUUACAUGGGGAUGACCCCGCGACUUGGAUUAGAGUCUCUUUUGGAAUAAGCCUGAAUGAUCCGAGUAGCAUCUCAG'
def condon(rna_seq):
    condon_seq = ''
    for n in range(0,len(rna_seq),3):   #遍历给定的序列，3个为一组
        if rna_seq[n:n+3] in condon_dict.keys():
            condon_seq += condon_dict[rna_seq[n:n+3]]
    return condon_seq
'''
file_input = open('rosalind_prot.txt','r')
rna = file_input.read()
file_output = open('rosalind_condon.txt','w')
file_output.write(condon(rna))
'''

print(condon(dna))
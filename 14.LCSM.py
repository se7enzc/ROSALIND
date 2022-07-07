'''
Finding a Shared Motif
Given: A collection of ( ) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
Sample Dataset：
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output：AC
'''
Rosalind_1 = 'GATTACA'
Rosalind_2 = 'TAGACCA'
Rosalind_3 = 'ATACA'
res = []
for i in range(len(Rosalind_3)):
    s_seq = Rosalind_3[i:]
    for j in range(len(s_seq)):
        res.append(s_seq[:(len(s_seq)-j)])
res.sort(key=len,reverse=True)
del res[-len(Rosalind_3):]  #删除单个碱基
res = list({}.fromkeys(res).keys())
print(res)
motif_list = []
for i in res:
    if i in Rosalind_1 and i in Rosalind_2:
        motif_list.append(i)
print(motif_list[0])

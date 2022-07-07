'''
Finding a Protein Motif
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, 
output its given access ID followed by a list of locations in the protein string where the motif can be found.
根据题目说明，得知N-glycosylation motif特征为3个氨基酸序列{P}[ST]{P}，表示第一氨基酸非P，第二个氨基酸为S或者T，第三个氨基酸为非P
'''
file_input = open('input.txt','r')
all_sequence_list = file_input.read().splitlines()  #逐行读取txt，并生成列表
sequence_list = {}
for i in range(0,len(all_sequence_list),2):
    sequence_list[all_sequence_list[i]] = all_sequence_list[(i+1)]

for key,value in sequence_list.items():
    print(key)
    aa_seqence = value
    aa_loc = ''
    for i in range(len(aa_seqence)-3):
        if aa_seqence[i] == 'N' and aa_seqence[(i+1)] != 'P' and aa_seqence[(i+2)] in ['S','T'] and aa_seqence[(i+3)] != 'P':
            aa_loc += str(i) + ' '
    if aa_loc == '' :
        aa_loc = 'None'
    print(aa_loc)
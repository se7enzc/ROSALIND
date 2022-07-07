#Genome Assembly as Shortest Superstring
file_input = open('input.txt','r')
all_sequence_list = file_input.read().splitlines()  #逐行读取txt，并生成列表
sequence_dict = {}
for i in range(0,len(all_sequence_list),2):
    sequence_dict[all_sequence_list[i]] = all_sequence_list[(i+1)]
print(sequence_dict)
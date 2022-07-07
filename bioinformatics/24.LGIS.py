#Longest Increasing Subsequence
'''
(8, 2, 1, 6, 5, 7, 4, 3, 9),(2, 6, 7, 9),(8, 6, 5, 4, 3)
输入：
5
5 1 4 2 3

输出：
1 2 3
5 4 2
'''
input_list = ['5','1','4','2','3']
up_list =[]
down_list = []
for i in range(len(input_list)):
    up_list.append(input_list[i])
    for j in range(i+1,len(input_list)):
        list1 = up_list.copy()
        for l in range(len(list1)):
            if int(input_list[j]) > int(list1[l][-1]):
                up_list.append(list1[l] + input_list[j])

for i in range(len(input_list)):
    down_list.append(input_list[i])
    for j in range(i+1,len(input_list)):
        list1 = down_list.copy()
        for l in range(len(list1)):
            if int(input_list[j]) < int(list1[l][-1]):
                down_list.append(list1[l] + input_list[j])

def debug(input,list_s):
    list1 = list_s.copy()
    for s in list1:
        list2 = list(s)
        for i in range(len(list2)-1):
            if input.index(list2[i]) > input.index(list2[i+1]):
                list_s.remove(s)
    return list_s

def longest_list(list1):
    list2 = []
    for i in list1:
        if len(i) == len(max(list1,key=len)):
            list2.append(i)
    return list2

up_list_mid = list(set(up_list))
down_list_mid = list(set(down_list))

up_list = debug(input_list,up_list_mid)
down_list = debug(input_list,down_list_mid)

longest_up_list = longest_list(up_list)
longset_down_list = longest_list(down_list)

[print(' '.join(x)) for x in longest_up_list]
[print(' '.join(x)) for x in longset_down_list]

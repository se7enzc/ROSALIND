#Enumerating k-mers Lexicographically
'''
A C G T
2
'''

#考虑到实际K值可能会较大，用递归思路

def mer(list,k):
    if k == 1 :
        return list
    else:
        sub_list = []
        for i in list:
            for j in mer(list,k-1):
                s = i + j
                sub_list.append(s)
    return sub_list

list = ['A','C','G','T']
print(mer(list,2))


#Enumerating Gene Orders
'''
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

def order(n):   # n≥2
    order_list = []
    for i in range(2,n+1):
        if i == 2:
            order_list.append('12')
            order_list.append('21')
        else:
            add = str(i)
            order_list_copy = order_list.copy()
            for s in order_list_copy:
                seq_s = add + s         #先加到最前面
                order_list.append(seq_s)
                seq_t = s + add         #再加到最后面
                order_list.append(seq_t)
                for x in range(1,i-1):
                    seq = s[:x] + add + s[x:]
                    order_list.append(seq)
            order_list_new = []
            for y in range(len(order_list)):
                if len(order_list[y]) == i:
                    order_list_new.append(order_list[y])
    return order_list_new
#print(order(3))
print(len(order(3)))
print(order(3))
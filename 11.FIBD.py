'''
The total number of pairs of rabbits that will remain after the x-th month if all rabbits live for y months.
变种的斐波那契数列
假设一对兔子只能存活y个月，即只能生育y-1次，x个月之后还剩多少对兔子？
假设第x月的幼年兔子为a^x，成年兔子为A^x，则有:
a^x = A^(x-1)
A^x = A^(x-1) + a^(x-1) - A^(x-y+1) = A^(x-1) + A^(x-2) - A^(x-y+1)
(a+A)^x = 2*A^(x-1) + A^(x-2) - A^(x-y+1)
'''
#这道题刚开始的思路被上面的备注误导了，单纯计算总兔子与成年兔子的关系没法使用递归，一定要计算每个月的总兔子之间的函数关系

x,y= 6,3

def rabbit(x,y):
    if x <= y:
        if x == 0:
            total = 1
        elif x == 1 :
            total = 1
        elif x == 2:
            total = 1
        else:
            total = rabbit(x-1,y) + rabbit(x-2,y)
    else:
        total = rabbit(x-1,y) + rabbit(x-2,y) - rabbit(x-y-1,y)
    return total

print(rabbit(6,3))

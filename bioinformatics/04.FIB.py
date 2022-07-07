'''The total number of rabbit pairs that will be present after 5 months,
if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of 3 rabbit pairs (instead of only 1 pair).
一对兔子达到繁殖年龄需要一个月,繁殖一次会生3对兔子,问开始有一对幼年兔子,5个月时共有多少对兔子
经典的菲波那切数列,f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2),黄金分割比例也由此得来,此题仅变化了下系数
即f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2)*3
'''
def rabbit_total(month,ratio):
    if month == 1 :
        rabbits = 1 #第一个月的时候只有一对幼年兔子
    elif month == 2:
        rabbits = 1 #第二个月的时候只有一对成年兔子
    else:
        rabbits = rabbit_total(month-1,ratio) + rabbit_total(month-2,ratio) * ratio
    return rabbits

print(rabbit_total(5,3))


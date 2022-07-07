'''
Independent Alleles
Given: Two positive integers k and N. 
In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation 
of Tom's family tree (don't count the Aa Bb mates at each level). 
Assume that Mendel's second law holds for the factors.
AaBb与AaBb杂交产生9种F1（9种基因型频率各不相同，AaBb为0.25），当9种F1再与AaBb杂交时，产生的后代中各基因型频率分布与F1代一致。
所以可以得到在第k代时，其中的任意个体基因型为AaBb的频率为0.25
'''
input = (2,1)
def p(k,n):
    num = 2**k
    n_p = 0
    for i in range(n):
        n_p += 0.25**i * 0.75**(num-i)
    return 1 - n_p

print(p(2,1))
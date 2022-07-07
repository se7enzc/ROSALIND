'''
Calculating Expected Offspring
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:

1.AA-AA 2.AA-Aa 3.AA-aa 4.Aa-Aa 5.Aa-aa 6.aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation,
under the assumption that every couple has exactly two offspring.
'''
#Sample Dataset:1 0 0 1 0 1 
#每个数字分别表示有多少对上文中配对的基因型
#Sample Output:3.5
#假设每对夫妇恰好有两个后代的情况下，下一代显示显性表型的后代的预期数量。
def ev_offspring(a,b,c,d,e,f):
    return(a*2 + b*2 + c*2 + d*1.5 + e + f*0)
print(ev_offspring(1,0,0,1,0,1))
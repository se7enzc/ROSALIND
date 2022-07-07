'''
孟德尔第一定律,AA、Aa、aa亲代得到的子代为显性表型的概率
原题表述有点绕，就是说有2个显性纯合，2个杂合子，2个隐形纯合，共有6名亲本，互相随机交配，计算产生子代显性表型的概率(AA or Aa)
input：2 2 2
output：0.78333
'''

#建立一个字典，key为亲本名称，value为亲本基因型
sample = {}
sample['hom_AA_1'] = sample['hom_AA_2'] = ['A','A']
sample['het_Aa_1'] = sample['het_Aa_2'] = ['A','a']
sample['hom_aa_1'] = sample['hom_aa_2'] = ['a','a']

#初始化
total_counts = 0
A_counts = 0

for key1 in sample:
    sample_F1 = sample[key1]        #获取第一个亲本，sample_1 = ['A','A']

    sample_copy = sample.copy()    #先建立一个sample副本，用copy函数而不是赋值，具体原因见函数说明
    del sample_copy[key1]            #已经选取一个亲本，再选择第二个亲本时就要去掉第一个亲本

    for key2 in sample_copy:
        sample_F2 = sample_copy[key2]    #获取第二个亲本，sample_2 = ['A','A']

        for a in sample_F1:             #从第一个亲本里中取出其中一个等位基因
            for b in sample_F2:          #从第二个亲本中去除一个等位基因，构成一个子代
                offspring = a + b
                total_counts += 1        #统计产生的每一个子代

                if offspring.find('A') != -1:   #统计显性表型子代(即包含有'A')的个数
                    A_counts += 1

print(A_counts/total_counts)
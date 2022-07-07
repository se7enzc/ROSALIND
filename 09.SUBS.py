'''
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset:GATATATGCATATACTT
                ATAT
Sample Output:2 4 10
'''
tar_seq = 'GATATATGCATATACTT'
motif_seq = 'ATAT'

def location(tar,motif):
    loc = ''
    lenth = len(motif)
    for n in range(0,len(tar)):
        if tar[n:n+lenth] == motif:
            loc += str(n+1) + ' '
    return loc

print(location(tar_seq,motif_seq))
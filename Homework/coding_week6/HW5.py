import string
UpperCase = string.ascii_uppercase
t = list(UpperCase)
d = {'A':0,'T':0,'G':0,'C':0}
def getBaseCounts2(dna):
    for i in dna:
        if i not in t :
            return 'The input DNA string is invalid'
        elif (i in ['A','T','G','C']):
            d[i] += 1
    return d            


def getBaseCounts(dna):
    #dna.split()
    d = dict()
    for c in dna:
        if c != 'A' and c != 'T' and c!='G' and c != 'C':
            return 'The input DNA string is invalid'
        elif c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

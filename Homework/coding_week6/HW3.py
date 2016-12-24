
def binaryToDecimal(binaryStr):
    t = list(binaryStr)
    p = []
    total = 0
    for i in t:
        i = int(i)
        p.append(i)
    for i in range(1, len(p)+1):
        total += p[i-1] * 2 ** (len(p) - i)
    return total
        

    

    
    

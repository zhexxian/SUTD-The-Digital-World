def extractValues(values):
    if len(values) % 2 != 0:
        a = len(values)/2
        no1 = int(values[0:a])
    else:
        a = len(values)/2
        no1 = int(values[0])
    no2 = int(values[a:2*a+1])
    return (no1,no2)
    




def calcRatios(tup):
    a = tup[0]
    b = tup[1]
    c = float(a)
    if b==0:
        return None
    else:
        return float(c/b)

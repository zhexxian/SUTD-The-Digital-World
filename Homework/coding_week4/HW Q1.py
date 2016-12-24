def C(F):
    C = (F - 32) * 5.0/9.0
    return round (C,1)

def CApprox(F):
    CApprox = (F - 30) / 2.0
    return round (CApprox, 2)

def getConversionTable():
    row1 = []
    row2 = []
    row3 = []
    for i in range (0, 101, 10):
        row1.append(i)
        row2.append(C(i))
        row3.append(CApprox(i))
    conversion=[row1,row2,row3]

    return conversion


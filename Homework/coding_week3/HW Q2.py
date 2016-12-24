

def tempConvert(string, number):
    if string == 'C':
        return fToC (number)
    elif string == 'F':
        return cToF (number)
    else:
        return None

def fToC(F):
    C = (F-32)*float(5)/9
    return C

def cToF(C):
    F = C*float(9)/5 + 32
    return F
    

def myReverse (t):
    rev = []
    l = len(t)
    n = l-1
    while n >= 0:
        rev.append(t[n])
        n -= 1
    return rev
    
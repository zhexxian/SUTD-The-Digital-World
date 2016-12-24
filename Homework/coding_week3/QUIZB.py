def printvals(n):
    t = []
    i = 1
    while i <= n:
        if i % 35.0 == 0.0:
            t.append('AB')
        elif i % 5.0 == 0.0:
            t.append('A')
        elif i % 7.0 == 0.0:
            t.append('B')
        else:
            t.append(i)
        i = i+1
    return t
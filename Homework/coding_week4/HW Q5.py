def diff(p):
    item1 = []
    item2 = []
    for i in p:
        if i >= 1:
            item1.append(i-1)
            item2.append(p[i] * i)
    return dict(zip(item1,item2))



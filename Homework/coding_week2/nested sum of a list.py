def nested_sum(t):
    res = []
    for s in t:
        if type(s) == int:
            res.append(s)
        if type(s) == list:
            res.append(sum(s))
    return sum(res)

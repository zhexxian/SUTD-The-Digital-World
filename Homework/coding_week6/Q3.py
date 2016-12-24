def reverse(s):
    a = ''
    i = 1
    while i <= len(s):
        a += s[-i]
        i+= 1
    return a


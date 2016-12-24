def palindrome(r):
    t = [int(d) for d in str(r)]
    s = t[:]
    s.reverse()

    return t == s
def is_anagram(a,b):
    a = list (a)
    b = list (b)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False
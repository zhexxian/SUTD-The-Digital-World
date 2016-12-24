def has_duplicates(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] == t[j] and j!= i:
                return True
    return False
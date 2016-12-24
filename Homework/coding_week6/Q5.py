def prefix(s1,s2):
    a = []
    delimiter = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            a.append(s1[i])
        else:
            break
    return delimiter.join(a)
   
    

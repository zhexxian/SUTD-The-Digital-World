def uncompressed(s):
    outp = []
    delimiter = ''
    for i in range(0,len(s),2):
        a = int(s[i])
        for j in range(a):
            outp.append(s[i+1])
    return delimiter.join(outp)
        

    
    

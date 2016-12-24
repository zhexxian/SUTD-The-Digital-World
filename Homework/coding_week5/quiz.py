def averageList(inp):
    outp = []
    for i in range (len(inp)):
        ave = int(sum(inp[i])/float(len(inp[i])))
        outp.append(ave)
    return outp

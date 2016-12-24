# Category A
'''
def stc(s1,s2):
    return abs(len(s1)-len(s2))

def sumVal(d):
    mysum = 0
    if d == {}:
        return None
    for s in d:
        if s < 3:
            mysum += d[s]
    return mysum

def count(a,b,c):
    return (b-a) > (c-b)

'''

# Category B
'''
f = open('mrt.txt','r')

def getMRT(f):
    dic = {}
    line = f.readline()
    while line:
        line = line.strip()
        w = line.split(',')
        dic[w[0]]=w[1:]
        line = f.readline()
    return dic

#Or


    for s in lines:
        s = s.strip()
        w = s.split(',')
        dic[w[0]]=w[1:]
    return dic

def distance(d,s):
    print d
    lists = s.split(',')
    print len(lists)
    if lists == []:
        return -2
    elif len(lists) != 2:
        return -1
    else:
        for i in d:
            if lists[0] in d[i] and lists[1] in d[i]:
                return abs(d[i].index(lists[0])-d[i].index(lists[1]))
        return -1

                
def diag(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            return False
    return True



def upperDiag(a):
    for i in range(1,len(a)):
        if a[i-1][i] == 0:
            return False
    return True
'''
def lowerDiag(a):
    for i in range(1,len(a)):
        if a[i][i-1] == 0:
            return False
    return True
m2=[[1,0,0,0], [3, 4, 1, 0], [0, 2, 3, 4], [0,0,1,3]] 

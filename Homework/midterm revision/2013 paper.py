'''

# Catergory A
n1 = input('enter first integer:')
n2 = input('enter second integer:')
out = []
for i in range(n1,n2+1,2):
    if n1%2 == 0:
        out.append(i+1)
    else:
        out.append(i)
print out



def findKey(d,s):
    for i in d:
        if i == s:
            return True
    return False


def check(s,n):
    try:
        return int(s) + int(n)
    except:
        return n




f = open('data.dat','r')
def getDict(f):
    dic = {}
    line = f.readline()
    while line:
        line = line.strip()
        line = line.split(' ')
        line[3] = float(line[3])
        key = line[0]
        dic[key] = line[1:]
        line = f.readline()
    return dic

def searchDict(d):
    e = raw_input('Enter an event:')
    if e in d:
        print '%s %s %s'%(d[e][0],d[e][1],d[e][2])
        searchDict(d)
    elif e == '*':
        print 'Bye!'
        return None
    else:
        print 'No such event'
        searchDict(d)


def test():
    f = open('data.dat','r')
    d = getDict(f)
    return searchDict(d)
    
'''    
# Dunno how to do Q1
'''
def seriesSummer(firstTerm, r, epsilon, termMax):
    s=firstTerm
    num=firstTerm
    lst=[firstTerm]
    
    a=1
    for i in range(1,termMax):
        num*=r
        lst.append(num)
        s+=num
        a+=1
        if num< epsilon:
            break
    if len(lst)<3:
        ans=lst
    else:
        ans=lst[-3::]        
    return (s,a,ans)
























def seriesSummer(firstTerm,r,epsilon,termMax):
    outsum = firstTerm
    count = 1
    lastThree = [firstTerm,firstTerm*r]
    while count < termMax:
        if abs(lastThree[-1]) < epsilon:
            break
        else:

            
            if count == 2:
                lastThree = [firstTerm,firstTerm*r, (lastThree[-1]*r)]
                
            elif count >= 3:
                lastThree = [lastThree[-2], (lastThree[-1]),(lastThree[-1] * r)]
             
            outsum += lastThree[-1]            
            count += 1
            
            
            
            
    return (outsum,count,lastThree)
'''      

'''

# Category A

a = input('Enter an integer:')
print 9*a



b = input('Enter a number:')
print round(b/9.0,2)



a = input('first number:')
b = input('second number:')
print a*b



x = input('expression:')
y = eval(str(x))
if type(y) == float:
    print round(y,2)
else:
    print y


# Category B

a = input('Enter an integer:')
if a >= 0:
    print 9 * a
else:
    print -9 * a


a=input('1st:')
b=input('2nd:')
c=input('3rd:')
maximum = a
for i in [a,b,c]:
    if i>maximum:
        maximum = i
print maximum


t = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
x = input('Enter an integer:')
if x >6 or x <0:
    print 'Incorrect input'
else:
    print t[x]


x = input('x:')
y = input('y:')
z = input('z:')
c1 = x<y and y>z+1
c2 = x<y and y>z+1 or x>0
c3 = not(x<y) or y>z or z>0
print 'C1: %s. C2: %s. C3: %s'%(c1,c2,c3)

# Category C

def minMax(n1,n2,m):
    if m == 0:
        return max(n1,n2)
    elif m == 1:
        return min(n1,n2)
    else:
        return None
        
        
from math import sin
from math import cos
def myEval(s,n1,n2):
    x = n1
    y = n2
    return eval(s)


def multGeneric(x,y):
    if type(x) == str:
        x = int(x)
    if type(y) == str:
        y = int(y)
    return x*y



def defaultFunc(x=5,y=6,z=7):
    return x*y*z

# Category D

def geometricSeries(n):
    i = 0
    s = 0
    while i < n:
        s += (2**i) / (float (3**i))
        i +=1
    return round(s,2)
# just check
def geometricSeries(e):
    i = 0
    s = 0
    while True:
        i +=1
        s +=(2**i) / (float (3**i))
        if (2**i) / (float (3**i)) < e:
            break           
    return s

def addEven(t):
    s = 0
    if t == []:
        return None
    else:
        for i in range(0,len(t),2):
            s += t[i]
        return s

def countZeroOne(t):
    out = [0,0]
    for i in t:
        if i == 0:
            out[0] += 1
        elif i == 1:
            out[1] += 1
    return tuple(out)


def flip(t):
    out = []
    for i in t:
        if i == 0:
            out.append(1)
        elif i == 1:
            out.append(0)
    return out
        


def convertDecimal(t):
    out = 0
    t.reverse()
    for i in range(len(t)):
        out += t[i] * (2 ** i)
    return out
        
    
def dnaBaseCount(s):
    out = [0,0,0,0]
    s = list(s)
    for i in s:
        if i == 'A':
            out[0]+=1
        elif i == 'C':
            out[1]+=1
        elif i == 'T':
            out[2]+=1
        elif i == 'G':
            out[3]+=1
    return out

def getData(count=0):
    a =input('Please enter an integer between 1 and 5:')
    if a >=1 and a <=5:
        return a
    elif (a<1 or a>5) and count < 2:
        count += 1
        getData(count)        
    else:
        return None
        
        
# Category F


def search(x,l):
    out = []
    for i in l:
        out.append(x in i)
    return out
           

def average(t):
    if t == []:
        return None
    return sum(t)/len(t)
def listAverage(t):
    out = []
    for i in t:
        out.append(average(i))
    return out

    
def matrixAdd(t1,t2):
    out = []
    for i in range(len(t1)):
        oh = []
        for j in range(len(t1[i])):
            oh.append(t1[i][j]+t2[i][j])
        out.append(oh)
    return out
   

def compare(t1,t2):
    return t1 == t2
# OR:


from copy import deepcopy
def compare(t1,t2):
    new1 = deepcopy(t1)
    new2 = deepcopy(t2)
    return not (new1 != new2)

# Category G
def createDict():
    dic = {}
    while True:
        a = raw_input('Enter a key:')
        if a == '*':
            break
        b = input('Enter a value:')
        dic[a] = b
    return dic


def dictSearch(d):
    inp = raw_input('Enter a key:')
    if inp not in d:
        return 'Sorry, %s is not in my dictionary'%(inp)
    elif inp == '*':
        return None
    else:
        print 'Capital of %s is %s'%(inp, d[inp])
        dictSearch(d)
        

def updateDict(d,l):
    dic = d
    for i in l:
        if i in d:
            del dic[i]
    return dic


def splitDict(d):
    out = []
    keys = []
    values = []
    for i in d:
        keys.append(i)
        values.append(d[i])
    out.append(keys)
    out.append(values)
    return out
# Category H


def countLines(name):
    fout = open(name,'r')
    count = 0
    line = fout.readline()
    while line:
        count += 1
        line = fout.readline()
    fout.close()
    return count
    


def createDict(name):
    fout = open(name,'r')
    line = fout.readline()
    dic = {}
    while line:
        (new1,new2) = line.split()
        dic[new1] = new2
        line = fout.readline()
        
        
    fout.close()                                    
    return dic    



def createFile(t,name):
    fout = open(name,'w')
    count = 0
    while count < len(t):
        fout.write(str(t[count])+'\n')
        count += 1
    fout.close()                                    
'''
fin = open('datain.dat','r')
fout = open('averagedata.dat','w') 
 
def readWriteFile(fin,fout):
    lines = fin.readlines()
    total = 0
    count = 0
    dictAverage = {}
    key = ''
    for s in lines:
        w = s.split()
        if len(w) == 1:
            if w[0] == '*':
                average = total / count
                total = 0
                count = 0
                
                dictAverage[key] = average
            else:
                key = w[0]
        elif len(lines) != 1:
            total += float(w[1])
            count += 1
        
    average = total / count
    dictAverage[key] = average
    print dictAverage
    
    s = ''
    
    for k in dictAverage:
        s += k
        s += ' %.2f \n'%(dictAverage[k])
    fout.write(s)
    fin.close()
    fout.close()

    
    
    
    
# -*- coding: utf-8 -*-

# COHORT EXERCISES
'''
# Q1
from math import sqrt
class Square(object):
    def __init__(self,length):
        self.length = length
    def getArea(self):
        return float(self.length **2)
    def setArea(self,area):
        self.length = sqrt(area)
    def __str__(self):
        return 'Square of height ''and'' width %s.'%(str(self.length))


# Q2
import time

class StopWatch:
    def __init__(self):
        self.startTime = time.time()
        self.endTime = -1
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def start(self):
        self.startTime = time.time()
        self.endTime = -1
    def stop(self):
        self.endTime = time.time()
    def getElapsedTime(self):
        if self.endTime == -1:
            return None
        else:
            return int((self.endTime - self.startTime)*1000)

    
# Q3
    
########## Define your class Line below this line ###########
class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    def __call__(self,x):
        return round(self.c0 + x*self.c1,1)
    def table(self,L,R,n):
        if n == 0:
            return 'Error in printing table'
        else:
            count = 0
            increment = (R - L)/float(n-1)
            x = round(L,2)
            result = ''
            while count < n:
                y = self.c0 + x*self.c1
                if x < 0 and y <0:
                    result += '     %.2f     %.2f\n'%(x,y)
                elif x< 0 and y>0:
                    result += '     %.2f      %.2f\n'%(x,y)
                elif x>0 and y<0:
                    result += '      %.2f     %.2f\n'%(x,y)
                elif len(str(int(y))) == 1:
                    result += '      %.2f      %.2f\n'%(x,y)

                else:

                    result += '      %.2f     %.2f\n'%(x,y)
                if R ==L:
                    break

                x += increment
                count += 1
            return result
        
        


########## Ignore the code below this line ##################

def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)

# HOMEWORK

# Q1
class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def setTime(self,elapseTime):
        self.hour = elapseTime / 3600
        self.minute = (elapseTime - self.hour*3600)/60
        self.second = (elapseTime - self.hour*3600 - self.minute *60)
        self.hour = self.hour%12
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second

    
# Q2
class Account:    
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
    def __str__(self):
        return '%s, %s, balance: %d'%(self.name,self.number,self.balance)
        




#  SOME PROBLEM
# Q3
from math import *
#return only the derivative value without rounding
#your return value is a float, which is the approximate value of the derivative
#Tutor will compute the approximate error based on your return value

x = 10.0
f = log
h = 1.0E-9

class Diff:

    def __init__(self,f,h):
        f = log(x)
        f1 = log(x+h)
        self.f = f
        self.f1 =f1
        self.h = h

    def __call__(self,x):
        self.x = x
        return (self.f1 - self.f)/float(self.h)
def f(x):
    return log(x)
df = Diff(f,h)
for x in (1,5,10):
    df_value = df(x)
exact = 1/float(x)
print "f'(%d)=%g (error=%.2E)" % (x, df_value, exact - df_value) 


    

# Q4
#For Test case 2: return a tuple with coeff list and evaluated value

class Polynomial:
    def __init__(self,coeff):
        self.coeff = coeff

        
    def __add__(self, other):
        longer = self.coeff
        shorter = other.coeff
        if len(longer) < len(other.coeff):
            longer = other.coeff
            shorter = self.coeff
        x = []
        for i in range(len(shorter)):
            x.append(longer[i]+shorter[i])
        if len(self.coeff) != len(other.coeff):
            for i in range(len(shorter),len(longer)):
                x.append(longer[i])

        return Polynomial(x)
    
    def __sub__(self, other):
        x = []
        longer = self.coeff
        shorter = other.coeff
        if len(longer) < len(other.coeff):
            longer = other.coeff
            shorter = self.coeff
        for i in range(len(shorter)):
            x.append(self.coeff[i]-other.coeff[i])
        if len(self.coeff) > len(other.coeff):
            for i in range(len(shorter),len(longer)):
                x.append(longer[i])
        elif len(self.coeff) < len(other.coeff):
            for i in range(len(shorter),len(longer)):
                x.append(0-longer[i])

        return Polynomial(x)
            
            
    def __call__(self,x):
        n = len(self.coeff)
        result = 0
        for i in range(n):
            result += self.coeff[i] * x**i
        return result
    def __mul__(self,other):
        dic = {}
        result = []
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                if (i+j) not in dic:
                    dic[i+j] = (self.coeff[i]*other.coeff[j])
                else:
                    dic[i+j] += (self.coeff[i]*other.coeff[j])
        for i in range(max(dic)+1):
            if dic[i] != {}:
                result.append(dic[i])
        return Polynomial(result)
        
    def differentiate(self):
        dic = {}
        result = []
        for i in range(len(self.coeff)):
            if (i-1) not in dic:
                dic[i-1] = (self.coeff[i]*i)
            else:
                dic[i-1] += (self.coeff[i]*i)
        for i in range(max(dic)+1):
            if dic[i] != {}:
                result.append(dic[i])
        self.coeff = result
        
    def derivative(self):
        dic = {}
        result = []
        for i in range(len(self.coeff)):
            if (i-1) not in dic:
                dic[i-1] = (self.coeff[i]*i)
            else:
                dic[i-1] += (self.coeff[i]*i)
        for i in range(max(dic)+1):
            if dic[i] != {}:
                result.append(dic[i])
        return Polynomial(result)


# EXERCISES

# Q1
from math import *
class F:
    def __init__(self,a,w):
        self.a=a
        self.w=w
        
    def value(self,x):
        return (exp(-self.a*x))*sin(self.w*x)
        
#f = F(a=1.0,w=0.1)

#print f.value(x=pi)
    
'''
# Q2
# be careful with potential integer division by 0

class Line0:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def value(self,x):
        gradiant = (self.p2[1]-self.p1[1])/float(self.p2[0]-self.p1[0])
        c = (self.p1[1] - gradiant * self.p1[0])
        return gradiant*x + c





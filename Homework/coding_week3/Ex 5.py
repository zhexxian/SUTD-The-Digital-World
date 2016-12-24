import math
def simpsonsRule(f,n,a,b):
    h = (b - a) / float(n)
    j= 2
    i=2
    fa = f (a + 2 * h)
    fb = f (a + h)
    while j <= (n/2 - 1):
        fa += f ( a + 2 * j * h) 
        j += 1 
    while i <= (n/2):
        fb += f (a + (2 * i - 1) * h)
        i += 1
        
    y = h/3.0 * (f(a) + 2 * fa + 4 * fb + f(b))
    return round (y, 2)
        
    

######### Ignore code below this line ######################################
def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)
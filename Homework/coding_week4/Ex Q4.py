import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def piApproxByMonteCarlo(numThrows):
    c = 0.0

    for i in range(numThrows):
        x=random.random()
        y=random.random()
        if (x-0.5)**2 + (y-0.5) **2 <= 0.25:
            c+=1

    return round(4*c/numThrows,2)
print piApproxByMonteCarlo(100000)
            


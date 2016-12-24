import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throwNdice(n, nExp):
    m = 0.0
    for i in range(0,n):
        for j in range(0,nExp):
            a=int(random.random() * 6)+1 
            if a == 6:
                m+=1
    result = float (m/(n*nExp))
    return round(result,2)
        

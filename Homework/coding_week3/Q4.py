
'''
import sys
a = -sys.maxint-1
b = sys.maxint
'''

'''
The Non-Ideal Way

def maxList(t):
    a = t[:]
    a.sort()
    b = a[:]
    b.reverse()
    
    return (a[0],b[0])
    
'''


#Why While Loop Doesn't Work

def maxList(t):
    i = 1
    MAX = t[0]
    while i < len(t):
        
        if MAX < t[i]:
            MAX = t[i]
        i = i + 1
    return MAX
    
print maxList([7,3,2,4,6,5])

'''
import sys

def maxList(t):
    if t == []:
        return (None, None)
    else:

        MAX = -sys.maxint-1
        MIN = sys.maxint
        i = 0
        while i < len(t):
            if t[i] >= MAX:
                MAX = t[i]
            if t[i] <= MIN:
                MIN = t[i]
            i = i+1
        return (MIN,MAX)

'''
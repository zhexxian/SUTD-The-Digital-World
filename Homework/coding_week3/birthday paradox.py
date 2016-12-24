def has_duplicates(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] == t[j] and j!= i:
                return True
    return False
    
from random import randint

t = []

for i in range(23):
    a = randint(1,365)
    t.append(a)
    
print has_duplicates(t)
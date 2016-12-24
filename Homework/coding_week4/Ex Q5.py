#### name your function game
import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def game(r, N):
    money = 0.0
    for i in range(N):
        x1 = random.randint(1,6)
        x2 = random.randint(1,6)
        x3 = random.randint(1,6)
        x4 = random.randint(1,6)
        if x1+x2+x3+x4 < 9:
            money += r - 1.0
        else:
            money -= 1.0
    if money > 0.0:
        return True
    else:
        return False

print game(10,10)

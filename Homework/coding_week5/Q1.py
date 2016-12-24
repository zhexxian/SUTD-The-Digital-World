import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def playCraps():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1+die2 in [2,3,12]:
        return 'You lose'
    elif die1+die2 in[7,11]:
        return 'You win'
    else:
        for i in 1000: #use while True
            die3 = random.randin(1,6)
            die4 = random.randin(1,6)
            if die3+die4 == 7:
                return 'You lose'
            elif die3+die4 == die1 + die2:
                return 'You win'
    

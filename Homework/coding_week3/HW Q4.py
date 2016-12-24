def isPrime (x):
    if x == 1 or x == 0:
        return False
    elif x == 2 or x == 3 or x == 5:
        return True
    elif x == 4:
        return False
    else:
        for i in range (2, x / 2 + 1):
            if x % i == 0:
                return False
                
        return True

# learning point: do not put else in for loop sometimes, 
# so that the loop will not stop right after first try
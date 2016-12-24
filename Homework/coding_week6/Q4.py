def isValidPassword(password):
    if len(password) < 8:
        return False
    a = 0
    for i in password:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            a+=1
        
    if a < 2:
        return False
    return True

    
    

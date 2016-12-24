def letterGrade(a):
    if a <= 100:
        if a >= 90:
            return 'A'
        elif a >= 80:
            return'B'
        elif a >= 70:
            return 'C'
        elif a >= 60:
            return 'D'
        elif a >= 0:
            return 'E'
    else:
        return None 
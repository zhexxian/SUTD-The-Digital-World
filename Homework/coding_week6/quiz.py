
def isValid(number):
    num = str(number)
    if len(num) not in [13,14,15,16]:
        return False

    elif (sumOfDoubleEvenPlace(number) + (sumOfOddPlace(number)))%10.0 == 0.0:
        return True
        
    else:
        return False





def sumOfDoubleEvenPlace(number):
    sumDE=0
    while number!=0:
        number/=10
        digit=number%10
        double=digit*2
        digitSum=getDigit(double)
        sumDE+=digitSum
        number/=10
    return sumDE

    

def getDigit(number):
    num = str(number)

    if len(num) == 1:
        return number
    elif len(num) == 2:

        return (int(num[0]) + int(num[1]))
    else:
        return 'Error'
    


def sumOfOddPlace(number):
    num = str(number)
    outp = 0
    for i in range (0,len(num),2):
        outp += int(num[len(num)-1-i])
    return outp
        
     


def prefixMatched(number, d):
    dnum = str(d)
    num = str(number)
    if len(dnum) == 1:
        return dnum == num[0]
    elif len(dnum) == 2:
        return dnum == num[0] + num[1]

def getSize(d):
    count=0
    while d!=0:
        count+=1
        d/=10
    return count    

def getPrefix(number,k):
    d=getSize(number)
    divisor=1
    for i in range(d-1-(k-1)):
        divisor*=10
    return number/divisor
